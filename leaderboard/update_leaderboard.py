import pandas as pd
import os

# -------------------------------
# FILE PATHS
# -------------------------------
LB_PATH = "docs/leaderboard.csv"
SUB_PATH = "submission.csv"

# -------------------------------
# LOAD FILES
# -------------------------------
if os.path.exists(LB_PATH):
    lb = pd.read_csv(LB_PATH)
else:
    lb = pd.DataFrame(columns=[
        "rank", "team", "f1_ideal", "f1_perturbed", "robustness_gap"
    ])

if not os.path.exists(SUB_PATH):
    raise FileNotFoundError("❌ submission.csv not found")

sub = pd.read_csv(SUB_PATH)

# -------------------------------
# VALIDATION
# -------------------------------
required_cols = ["team", "f1_ideal", "f1_perturbed"]
for col in required_cols:
    if col not in sub.columns:
        raise Exception(f"Missing column: {col}")

# -------------------------------
# COMPUTE METRICS
# -------------------------------
sub["robustness_gap"] = sub["f1_ideal"] - sub["f1_perturbed"]

# -------------------------------
# UPDATE LEADERBOARD
# -------------------------------
lb = pd.concat([lb, sub], ignore_index=True)

# Keep BEST score per team
lb = lb.sort_values(by="f1_ideal", ascending=False)
lb = lb.drop_duplicates(subset="team", keep="first")

# Assign ranks
lb = lb.reset_index(drop=True)
lb["rank"] = lb.index + 1

# Reorder columns
lb = lb[["rank", "team", "f1_ideal", "f1_perturbed", "robustness_gap"]]

# -------------------------------
# SAVE
# -------------------------------
lb.to_csv(LB_PATH, index=False)

print("🏆 Leaderboard updated!")
print(lb.head())
