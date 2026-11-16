# Lab 4 - Dynamic Programming (ENCA351)

K.R. Mangalam University, School of Engineering and Technology.
Aditya Shibu (2401201047), BCA (AI & DS) Sec B. Faculty: Dr. Aarti Sangwan.

Three dynamic programs with time, memory and state counts: Longest Common
Subsequence, 0/1 Knapsack and Matrix Chain Multiplication, plus a naive
recursion against the table on the same LCS inputs.

## Structure

```text
.
├── README.md
├── lcs.py                  # DP table, rebuild, naive recursion
├── knapsack_dp.py          # 0/1 table, chosen set, one-row variant
├── matrix_chain.py         # interval DP, split table, parenthesization
├── app.py                  # interactive menu for the three programs
├── run_experiments.py      # medians -> data/experiments.csv + recursive_vs_dp.csv
├── make_plots.py           # six figures -> graphs/
├── requirements.txt
├── krmu_logo.png           # report front page
├── Aditya_Shibu_2401201047_ENCA351_Lab4.md  # report source
├── Aditya_Shibu_2401201047_ENCA351_Lab4.pdf # report (22 pp)
├── Lab4_Performance_Complexity_Aditya_Shibu_2401201047.pdf  # slot 1 (4 pp)
├── Lab4_Graphs_Visualizations_Aditya_Shibu_2401201047.pdf   # slot 2 (5 pp)
├── graphs/                 # runtime, memory, heatmaps, recursion vs DP
├── data/                   # experiments.csv (17 rows), recursive_vs_dp.csv
└── screenshots/            # terminal evidence
```

## Submission files

| Slot | File | Pages |
|---|---|---|
| 1. Execution time, memory, subproblems, complexity table | `Lab4_Performance_Complexity_Aditya_Shibu_2401201047.pdf` | 4 |
| 2. Visualizations, runtime graphs, heatmaps | `Lab4_Graphs_Visualizations_Aditya_Shibu_2401201047.pdf` | 5 |
| 3. Complete Lab 4 report | `Aditya_Shibu_2401201047_ENCA351_Lab4.pdf` | 22 |

The two pieces are slices of the complete report: front page, complexity
section and the three measurement tables for slot 1; front page, both
scaling charts, the recursion comparison and the three DP table heatmaps for
slot 2.

## Run

```bash
python lcs.py
python knapsack_dp.py
python matrix_chain.py
python app.py
python run_experiments.py
python make_plots.py
```

## Module map

| File | Brief task |
|---|---|
| `lcs.py` | table, subsequence rebuild, naive recursion with call count |
| `knapsack_dp.py` | bottom-up table, reconstruction, O(C) one-row check |
| `matrix_chain.py` | interval DP, split table, parenthesization |
| `app.py` | interactive menu for LCS, knapsack and matrix chain |
| `run_experiments.py` | timed runs with tracemalloc off, memory runs with it on |
| `make_plots.py` | scaling curves, three heatmaps, recursion comparison |

## Report

Full write-up with tasks, code, recurrences, tables, heatmaps, discussion and
the recursion versus DP comparison:
`Aditya_Shibu_2401201047_ENCA351_Lab4.pdf` (22 pp, verified clean), plus the
two slot pieces listed above.
