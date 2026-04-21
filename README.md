# Graph-Robustness-Checker-using-Logistic-Regression

##  Overview

This project simulates a **graph classification robustness challenge**, where models are evaluated under:

-  Clean (Ideal) features  
-  Noisy (Perturbed) features  

The goal is to build models that are **accurate + robust under noise**.

---

 ##  Live Leaderboard
 [Open Leaderboard](https://vforviolet10.github.io/Graph-Robustness-Checker-using-Logistic-Regression/)

---

---

##  Objective

Participants must generate predictions for:

1. **Ideal Dataset (clean features)**
2. **Perturbed Dataset (noisy features)**

---

##  Evaluation Metrics

We compute:

-  F1 Score (Ideal)
-  F1 Score (Perturbed)
-  Robustness Gap

### Formula:

```

Robustness Gap = F1_ideal − F1_perturbed

```


##  Model

Baseline model:

- Logistic Regression (Scikit-learn)
- Fast + interpretable + strong baseline

---

##  Perturbation Strategy

To simulate real-world noise:

### Feature Shift
```

x ← x + 0.3

```

### Gaussian Noise
```

x ← x + N(0, 0.05)

```

---

##  Submission Format (IMPORTANT)

###  Do NOT submit rank manually

###  Correct format:

```

team,f1_ideal,f1_perturbed,robustness_gap

````

### Example:

```csv
Team_Alpha,0.91,0.86,0.05
````

---

##  Submission Workflow (PR SYSTEM)

1. Fork the repository
2. Add your submission file
3. Create a Pull Request
4. Automated evaluation runs
5. Leaderboard updates automatically

---

##  Leaderboard Format

```
team,f1_ideal,f1_perturbed,robustness_gap
TeamA,0.91,0.85,0.06
TeamB,0.89,0.87,0.02
```

---

##  Getting Started

### Install dependencies

```bash
pip install pandas numpy scikit-learn streamlit
```

---

### Run baseline model

```bash
python starter_code/baseline.py
```


---

## Rules

* Do NOT modify `test_labels_hidden.csv`
* Do NOT manually edit leaderboard
* Keep team names unique
* Ensure correct CSV format

---


##  License

MIT License — open for academic and hackathon use.

---

Updated for PR


