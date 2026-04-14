import pandas as pd
import os

# File path
file_path = "docs/leaderboard.csv"

# Load leaderboard (create if not exists)
if os.path.exists(file_path):
    lb = pd.read_csv(file_path)
else:
    lb = pd.DataFrame(columns=["team", "f1_ideal", "f1_perturbed", "gap"])

# Team name from PR
team_name = os.getenv("GITHUB_ACTOR", "Unknown")

# 🔥 Replace with real evaluation later
f1_ideal = 0.90
f1_perturbed = 0.85
gap = round(f1_ideal - f1_perturbed, 4)

# Create new row
new_row = {
    "team": team_name,
    "f1_ideal": f1_ideal,
    "f1_perturbed": f1_perturbed,
    "gap": gap
}

# ❗ Remove old entry of same team (avoid duplicates)
lb = lb[lb["team"] != team_name]

# Add new row
lb = pd.concat([lb, pd.DataFrame([new_row])], ignore_index=True)

# ✅ Sort: lowest gap is best
lb = lb.sort_values(by="gap", ascending=True)

# Save
lb.to_csv(file_path, index=False)
