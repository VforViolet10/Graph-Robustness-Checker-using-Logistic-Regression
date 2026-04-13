import os
import pandas as pd
from evaluate import evaluate

LEADERBOARD_PATH = "leaderboard/leaderboard.csv"
SUBMISSIONS_PATH = "submissions"

def update_leaderboard():
    results = []

    for team in os.listdir(SUBMISSIONS_PATH):
        team_path = os.path.join(SUBMISSIONS_PATH, team)

        if os.path.isdir(team_path):
            try:
                f1_i, f1_p, gap = evaluate(team_path)

                results.append({
                    "team": team,
                    "f1_ideal": f1_i,
                    "f1_perturbed": f1_p,
                    "gap": gap
                })

            except Exception as e:
                print(f" Error in {team}: {e}")

    df = pd.DataFrame(results)

    # GTA Ranking Logic:
    df = df.sort_values(
        by=["f1_perturbed", "gap"],
        ascending=[False, True]
    )

    df.to_csv(LEADERBOARD_PATH, index=False)
    print(" Leaderboard Updated!")

if __name__ == "__main__":
    update_leaderboard()
