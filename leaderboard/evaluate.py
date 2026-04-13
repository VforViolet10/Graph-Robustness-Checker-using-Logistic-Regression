import pandas as pd
from sklearn.metrics import accuracy_score

# Load files
y_true = pd.read_csv("data/test.csv")
y_pred = pd.read_csv("submission.csv")

# Calculate score
score = accuracy_score(y_true["target"], y_pred["target"])

# Get username
import os
username = os.getenv("GITHUB_ACTOR")

# Load leaderboard
lb = pd.read_csv("data/leaderboard.csv")

# Append new score
new_row = pd.DataFrame([{
    "username": username,
    "score": score
}])

lb = pd.concat([lb, new_row])

# Sort leaderboard
lb = lb.sort_values(by="score", ascending=False)

# Save
lb.to_csv("data/leaderboard.csv", index=False)
