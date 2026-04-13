import os
import pandas as pd
from evaluate import evaluate
from datetime import datetime

LEADERBOARD_PATH = "leaderboard/leaderboard.csv"
SUBMISSIONS_PATH = "submissions"

def update_leaderboard():
    results = []

    for team in os.listdir(SUBMISSIONS_PATH):
        team_path = os.path.join(SUBMISSIONS_PATH, team)

        if os.path.isdir(team_path):
            try:
                # -------- VALIDATION --------
                ideal_path = os.path.join(team_path, "ideal_submission.csv")
                perturbed_path = os.path.join(team_path, "perturbed_submission.csv")

                if not os.path.exists(ideal_path) or not os.path.exists(perturbed_path):
                    raise ValueError("Missing submission files")

                ideal_df = pd.read_csv(ideal_path)
                perturbed_df = pd.read_csv(perturbed_path)

                required_cols = {"graph_index", "label"}

                if not required_cols.issubset(ideal_df.columns):
                    raise ValueError("Invalid ideal_submission format")

                if not required_cols.issubset(perturbed_df.columns):
                    raise ValueError("Invalid perturbed_submission format")

                # -------- EVALUATION --------
                f1_i, f1_p, gap = evaluate(team_path)

                results.append({
                    "team": team,
                    "f1_ideal": f1_i,
                    "f1_perturbed": f1_p,
                    "gap": gap,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })

            except Exception as e:
                print(f" Error in {team}: {e}")

    df = pd.DataFrame(results)

    # -------- SORTING (GTA STYLE) --------
    df = df.sort_values(
        by=["f1_perturbed", "gap"],
        ascending=[False, True]
    )

    # -------- KEEP BEST ONLY --------
    df = df.drop_duplicates(subset=["team"], keep="first")

    df.to_csv(LEADERBOARD_PATH, index=False)
    print(" Leaderboard Updated!")

if __name__ == "__main__":
    update_leaderboard()
