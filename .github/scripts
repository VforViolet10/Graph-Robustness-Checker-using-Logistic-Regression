from pathlib import Path
import subprocess
import sys

repo_root = Path(__file__).parent.parent.parent.resolve()

def main():
    python_exe = sys.executable

    submissions_dir = repo_root / "submissions"
    print(f"Submissions directory: {submissions_dir}")

    if not submissions_dir.exists():
        print("No submissions found.")
        return

    print("Scoring submissions (Ideal + Perturbed)...")

    subprocess.run(
        [python_exe, str(repo_root / "leaderboard/calculate_scores.py")],
        check=True
    )

    print("✅ Leaderboard updated!")

if __name__ == "__main__":
    main()
