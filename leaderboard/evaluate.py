import pandas as pd
from sklearn.metrics import f1_score

def evaluate(team_folder):
    # Load true labels
    true = pd.read_csv("data/test_labels_hidden.csv")

    # Load submissions
    ideal = pd.read_csv(f"{team_folder}/ideal_submission.csv")
    perturbed = pd.read_csv(f"{team_folder}/perturbed_submission.csv")

    # Merge
    ideal = ideal.merge(true, on="graph_index")
    perturbed = perturbed.merge(true, on="graph_index")

    # Compute F1
    f1_ideal = f1_score(ideal["label_y"], ideal["label_x"], average="macro")
    f1_perturbed = f1_score(perturbed["label_y"], perturbed["label_x"], average="macro")

    gap = f1_ideal - f1_perturbed

    return round(f1_ideal, 4), round(f1_perturbed, 4), round(gap, 4)
