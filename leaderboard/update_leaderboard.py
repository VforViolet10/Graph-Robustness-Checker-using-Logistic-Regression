import pandas as pd
import os
import glob
import json

LB_PATH = "docs/leaderboard.json"
SUB_FOLDER = "submission/*.csv"

# -----------------------------

# Load existing leaderboard

# -----------------------------

if os.path.exists(LB_PATH):
with open(LB_PATH) as f:
lb = json.load(f)
else:
lb = []

# -----------------------------

# Read all submissions

# -----------------------------

files = glob.glob(f"{SUB_FOLDER}/*.csv")

if not files:
raise Exception("No submissions found")

all_subs = []

for file in files:
df = pd.read_csv(file)
all_subs.append(df)

sub = pd.concat(all_subs, ignore_index=True)

# -----------------------------

# Validation

# -----------------------------

required = ["team", "f1_ideal", "f1_perturbed"]

for col in required:
if col not in sub.columns:
raise Exception(f"Missing column: {col}")

# -----------------------------

# Compute robustness gap

# -----------------------------

sub["robustness_gap"] = sub["f1_ideal"] - sub["f1_perturbed"]

# -----------------------------

# Keep best per team

# -----------------------------

sub = sub.sort_values(by="f1_ideal", ascending=False)
sub = sub.drop_duplicates(subset="team", keep="first")

# -----------------------------

# Convert to leaderboard format

# -----------------------------

sub = sub.reset_index(drop=True)

leaderboard = []

for i, row in sub.iterrows():
leaderboard.append({
"group": row["team"],
"f1_score": float(row["f1_ideal"]),
"f1_perturbed": float(row["f1_perturbed"]),
"robustness_gap": float(row["robustness_gap"]),
"pr": i + 1
})

# -----------------------------

# Save leaderboard

# -----------------------------

with open(LB_PATH, "w") as f:
json.dump(leaderboard, f, indent=2)

print("🏆 Leaderboard updated successfully!")
