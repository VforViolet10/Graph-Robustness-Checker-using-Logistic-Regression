import pandas as pd
import os

# Load leaderboard
lb_path = "docs/leaderboard.csv"

if os.path.exists(lb_path):
    lb = pd.read_csv(lb_path)
else:
    lb = pd.DataFrame(columns=["team", "f1_ideal", "f1_perturbed", "robustness_gap"])

# Get submission file
sub = pd.read_csv("submission.csv")

# Calculate robustness gap
sub["robustness_gap"] = sub["f1_ideal"] - sub["f1_perturbed"]

# Append
lb = pd.concat([lb, sub], ignore_index=True)

# Sort leaderboard
lb = lb.sort_values(by="f1_ideal", ascending=False)

# Save
lb.to_csv(lb_path, index=False)

print("Leaderboard updated!")
