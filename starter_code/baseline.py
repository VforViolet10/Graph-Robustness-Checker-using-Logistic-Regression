import os
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# ----------------------------
# Paths
# ----------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR))

DATA_DIR = os.path.join(REPO_ROOT, "data")
SUBMISSIONS_DIR = os.path.join(REPO_ROOT, "submissions")

os.makedirs(SUBMISSIONS_DIR, exist_ok=True)

# ----------------------------
# Load Data
# ----------------------------

train = pd.read_csv(os.path.join(DATA_DIR, "train.csv"))
test = pd.read_csv(os.path.join(DATA_DIR, "test.csv"))

# ----------------------------
# Features & Labels
# ----------------------------

X_train = train.drop(columns=["label", "graph_index"])
y_train = train["label"]

X_test = test.drop(columns=["graph_index"])

# ----------------------------
# Scaling (Improves robustness)
# ----------------------------

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ----------------------------
# Model
# ----------------------------

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# ----------------------------
# Ideal Predictions
# ----------------------------

ideal_preds = model.predict(X_test)

# ----------------------------
# Perturbation Function
# ----------------------------

def perturb(data, shift=0.3, noise=0.05):
    return data + shift + np.random.normal(0, noise, data.shape)

# ----------------------------
# Perturbed Predictions
# ----------------------------

X_test_perturbed = perturb(X_test)
perturbed_preds = model.predict(X_test_perturbed)

# ----------------------------
# Save Submissions
# ----------------------------

ideal_path = os.path.join(SUBMISSIONS_DIR, "ideal_submission.csv")
perturbed_path = os.path.join(SUBMISSIONS_DIR, "perturbed_submission.csv")

pd.DataFrame({
    "graph_index": test["graph_index"],
    "label": ideal_preds
}).to_csv(ideal_path, index=False)

pd.DataFrame({
    "graph_index": test["graph_index"],
    "label": perturbed_preds
}).to_csv(perturbed_path, index=False)

print("✅ Done! Submissions saved.")
print("Ideal:", ideal_path)
print("Perturbed:", perturbed_path)
