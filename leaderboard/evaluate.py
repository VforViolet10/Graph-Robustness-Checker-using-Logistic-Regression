import pandas as pd
import numpy as np
import os

# -------------------------------
# CONFIG
# -------------------------------
TEAM_NAME = os.getenv("GITHUB_ACTOR", "unknown_team")

# -------------------------------
# DUMMY EVALUATION (replace later)
# -------------------------------
# Simulating model performance

np.random.seed(42)

f1_ideal = np.round(np.random.uniform(0.85, 0.95), 4)
f1_perturbed = np.round(f1_ideal - np.random.uniform(0.02, 0.08), 4)

# -------------------------------
# CREATE SUBMISSION
# -------------------------------
submission = pd.DataFrame([{
    "team": TEAM_NAME,
    "f1_ideal": f1_ideal,
    "f1_perturbed": f1_perturbed
}])

# Save file
submission.to_csv("submission.csv", index=False)

print("✅ Submission file created:")
print(submission)
