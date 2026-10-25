# Lab 3 - Smart Resource Allocation and Scheduling System (ENCA351)

K.R. Mangalam University, School of Engineering and Technology.
Aditya Shibu (2401201047), BCA (AI & DS) Sec B. Faculty: Dr. Aarti Sangwan.

Three greedy algorithms with time and memory measurements: Fractional
Knapsack, Activity Selection and Huffman Coding, plus the 0/1 knapsack
counterexample where the ratio rule fails.

## Structure

```text
.
├── README.md
├── fractional_knapsack.py  # ratio greedy, 0/1 greedy, exact 0/1 check
├── activity_selection.py   # earliest-finish greedy
├── huffman_coding.py       # min-heap tree, prefix codes, encode/decode
├── run_experiments.py      # 5-run medians -> data/experiments.csv
├── make_plots.py           # five figures -> graphs/
├── requirements.txt
├── krmu_logo.png           # report front page
├── Aditya_Shibu_2401201047_ENCA351_Lab3.md  # report source
├── Aditya_Shibu_2401201047_ENCA351_Lab3.pdf # report (20 pp)
├── Lab3_Performance_Complexity_Aditya_Shibu_2401201047.pdf  # slot 1 (4 pp)
├── Lab3_Graphs_Visualizations_Aditya_Shibu_2401201047.pdf   # slot 2 (5 pp)
├── graphs/                 # scaling, allocation, timeline, tree
├── data/                   # experiments.csv (21 rows)
└── screenshots/            # terminal evidence
```

## Submission files

| Slot | File | Pages |
|---|---|---|
| 1. Execution time, memory, complexity table | `Lab3_Performance_Complexity_Aditya_Shibu_2401201047.pdf` | 4 |
| 2. Visualizations and performance graphs | `Lab3_Graphs_Visualizations_Aditya_Shibu_2401201047.pdf` | 5 |
| 3. Complete Lab 3 report | `Aditya_Shibu_2401201047_ENCA351_Lab3.pdf` | 20 |

The two pieces are slices of the complete report: front page, then the
complexity section plus the time and memory tables for slot 1; front page,
then the performance, allocation, timeline and Huffman tree pages for slot 2.

## Run

```bash
python fractional_knapsack.py
python activity_selection.py
python huffman_coding.py
python run_experiments.py
python make_plots.py
```

## Module map

| File | Brief task |
|---|---|
| `fractional_knapsack.py` | ratio greedy, split the last item; 0/1 failure check |
| `activity_selection.py` | earliest-finish selection |
| `huffman_coding.py` | tree build, code table, encode and decode |
| `run_experiments.py` | sizes 100 to 10000, median time and peak memory |
| `make_plots.py` | performance, allocation, timeline and tree figures |

## Report

Full write-up with tasks, code, proofs sketches, tables, figures, discussion
and the greedy failure case:
`Aditya_Shibu_2401201047_ENCA351_Lab3.pdf` (20 pp, verified clean), plus the
two slot pieces listed above.
