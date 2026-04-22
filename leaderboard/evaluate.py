import pandas as pd
import numpy as np
import json
import os

# -------------------------------

# CONFIG

# -------------------------------

TEAM_NAME = os.getenv("GROUP_NAME", "unknown_team")

# -------------------------------

# LOAD SUBMISSION

# -------------------------------

submission_files = [f for f in os.listdir("submission") if f.endswith(".csv")]

if not submission_files:
print("❌ No submission file found")
exit(1)

submission_path = os.path.join("submission", submission_files[0])
sub = pd.read_csv(submission_path)

# -------------------------------

# VALIDATION

# -------------------------------

required_cols = ["prediction"]

for col in required_cols:
if col not in sub.columns:
print(f"❌ Missing column: {col}")
exit(1)

# -------------------------------

# DUMMY SCORING (Replace later)

# -------------------------------

np.random.seed(len(sub))  # deterministic per submission size

f1_ideal = np.round(np.random.uniform(0.85, 0.95), 4)
f1_perturbed = np.round(f1_ideal - np.random.uniform(0.02, 0.08), 4)

robustness_gap = np.round(f1_ideal - f1_perturbed, 4)

# Final score (you can tweak this formula)

final_score = np.round(f1_perturbed - robustness_gap * 0.5, 4)

print(f"✅ Ideal F1: {f1_ideal}")
print(f"⚠️ Perturbed F1: {f1_perturbed}")
print(f"📉 Robustness Gap: {robustness_gap}")
print(f"🏆 Final Score: {final_score}")

# -------------------------------

# SAVE RESULT

# -------------------------------

result = {
"group": TEAM_NAME,
"f1_score": float(final_score),
"f1_ideal": float(f1_ideal),
"f1_perturbed": float(f1_perturbed),
"robustness_gap": float(robustness_gap)
}

os.makedirs("grader", exist_ok=True)

with open("grader/result.json", "w") as f:
json.dump(result, f)

print("📁 Result saved to grader/result.json")
