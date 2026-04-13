# Graph-Robustness-Checker-using-Logistic-Regression

A lightweight machine learning project to evaluate **model robustness under feature perturbations**, inspired by large-scale ML competitions.

---

 ## 🏆 Live Leaderboard
 [Open Leaderboard](https://vforviolet10.github.io/Graph-Robustness-Checker-using-Logistic-Regression/)

## Overview

This project simulates a **graph classification challenge** where models are evaluated under two conditions:

*  **Ideal Setting** – clean, unmodified features
*  **Perturbed Setting** – features corrupted with noise and distribution shift

The goal is to build models that are **accurate and robust**.

---

## Objective

Participants must generate predictions for:

1. **Ideal Dataset** (clean features)
2. **Perturbed Dataset** (noisy features)

The system evaluates:

*  **F1 Score (Ideal)**
*  **F1 Score (Perturbed)**
*  **Robustness Gap**

> **Robustness Gap = F1_ideal − F1_perturbed**

---

## Project Structure

```
graph-robustness-ml/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── test_labels_hidden.csv   # (used only for evaluation)
│
├── submissions/
│   └── <Team_Name>/
│       ├── ideal_submission.csv
│       └── perturbed_submission.csv
│
├── leaderboard/
│   ├── evaluate.py
│   ├── update_leaderboard.py
│   └── leaderboard.csv
│
├── starter_code/
│   └── baseline.py
│
├── app.py                # Streamlit leaderboard UI (optional)
├── README.md
```

---

## Dataset Description

Each row represents a graph using simplified numerical features:

| Feature     | Description           |
| ----------- | --------------------- |
| graph_index | Unique graph ID       |
| nodes       | Number of nodes       |
| edges       | Number of edges       |
| avg_degree  | Average node degree   |
| label       | Target class (0 or 1) |

---

## Model

Baseline model uses:

* Logistic Regression (from **Scikit-learn**)
* Fast, interpretable, and effective for small datasets

---

## Perturbation Mechanism

To simulate real-world noise:

* **Feature Shift:**

  ```
  x ← x + 0.3
  ```

* **Gaussian Noise:**

  ```
  x ← x + N(0, 0.05)
  ```

This tests whether models generalize beyond clean data.

---

## Evaluation Metrics

We use **Macro F1 Score**:

* Handles class imbalance
* Balances precision & recall

### Final Ranking Criteria

1. Highest **F1 Score (Perturbed)**
2. Lowest **Robustness Gap**
3. Latest submission (optional)

---

## Getting Started

### 1️.Install Dependencies

```bash
pip install pandas numpy scikit-learn streamlit
```

---

### 2️.Run Baseline Model

```bash
python starter_code/baseline.py
```

This generates:

```
submissions/
├── ideal_submission.csv
└── perturbed_submission.csv
```


### 3️.Submit Predictions

Create a team folder:

```
submissions/YourTeamName/
```

Move your files:

```
ideal_submission.csv
perturbed_submission.csv
```


### 4️.Update Leaderboard

```bash
python leaderboard/update_leaderboard.py
```


### 5️.View Leaderboard (Optional UI)

```bash
streamlit run app.py
```

---

## Leaderboard Format

```
team,f1_ideal,f1_perturbed,gap
TeamA,0.91,0.85,0.06
TeamB,0.89,0.87,0.02
```


## Submission Format

### ideal_submission.csv

```
graph_index,label
1,0
2,1
3,0
```

### perturbed_submission.csv

```
graph_index,label
1,0
2,1
3,1
```


## Notes

* Do **NOT** modify `test_labels_hidden.csv`
* Ensure correct column names
* Team folder names should not contain spaces


## Future Improvements

* Add Random Forest / XGBoost models
* Introduce real graph datasets (e.g., MUTAG)
* Deploy leaderboard online
* Add encryption-based submissions


## License

This project is open-source under the MIT License.
