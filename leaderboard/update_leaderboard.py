import pandas as pd
import os
import glob

LB_PATH = "docs/leaderboard.json"
SUB_FOLDER = "submissions"

# Load leaderboard
if os.path.exists(LB_PATH):
    lb = pd.read_csv(LB_PATH)
else:
    lb = pd.DataFrame(columns=["team", "f1_ideal", "f1_perturbed", "robustness_gap"])

# Read ALL submissions
files = glob.glob(f"{SUB_FOLDER}/*.csv")

all_subs = []

for file in files:
    df = pd.read_csv(file)
    all_subs.append(df)

if not all_subs:
    raise Exception("No submissions found")

sub = pd.concat(all_subs, ignore_index=True)

# Compute robustness gap if not present
if "robustness_gap" not in sub.columns:
    sub["robustness_gap"] = sub["f1_ideal"] - sub["f1_perturbed"]

# Keep best per team
sub = sub.sort_values(by="f1_ideal", ascending=False)
sub = sub.drop_duplicates(subset="team", keep="first")

# Add rank
sub = sub.reset_index(drop=True)
sub["rank"] = sub.index + 1
sub = sub.rename(columns={
    "team": "group",
    "f1_ideal": "f1_score"
})

sub["pr"] = sub["rank"]

# Reorder
sub = sub[["rank", "team", "f1_ideal", "f1_perturbed", "robustness_gap"]]

# Save leaderboard
sub.to_json(LB_PATH, orient="records", indent=4)
print("🏆 Leaderboard updated successfully!")
