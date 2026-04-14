import pandas as pd
import os

# Load leaderboard
lb = pd.read_csv("docs/leaderboard.csv")

# Example: fake score (replace with real evaluation)
new_row = {
    "team": os.getenv("GITHUB_ACTOR"),
    "f1_ideal": 0.90,
    "f1_perturbed": 0.85,
    "robustness_gap": 0.05
}

lb = pd.concat([lb, pd.DataFrame([new_row])])

lb = lb.sort_values(by="f1_perturbed", ascending=False)

lb.to_csv("docs/leaderboard.csv", index=False)
