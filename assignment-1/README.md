# Lab 1 - Sorting and Fibonacci Efficiency Analysis (ENCA301)

K.R. Mangalam University, School of Engineering and Technology.
Aditya Shibu (2401201047), BCA (AI & DS) Sec B. Submitted to Dr. Aarti Sangwan.

Comparative study of sorting (bubble, insertion, merge, quick) and Fibonacci
(recursive, iterative, DP) efficiency across input sizes and conditions.

## Structure

```text
.
├── README.md
├── algorithms/
│   ├── sorting.py      # bubble, insertion, merge, quick sort
│   └── fibonacci.py    # recursive, iterative, DP
├── analysis/
│   ├── performance.py  # 5-run median time + memory harness
│   └── visualizations.py
├── notebook/
│   ├── algorithm_efficiency_analysis.ipynb
│   └── run_analysis.py # full pipeline driver
├── graphs/             # sorting + fibonacci charts
├── data/               # sorting_performance.csv, fibonacci_performance.csv
├── screenshots/        # terminal evidence + image-57.png (report logo)
├── requirements.txt
├── Lab1_Aditya_Shibu_2401201047.md  # report source
├── Lab1_Aditya_Shibu_2401201047.pdf # full report (46 pp)
├── Lab1_Experimental_Analysis_Aditya_Shibu_2401201047.pdf
├── Lab1_Complexity_Table_Aditya_Shibu_2401201047.pdf
└── Lab1_Graphs_Visualizations_Aditya_Shibu_2401201047.pdf
```

## Run

```bash
python notebook/run_analysis.py
```

## Module map

| File | Purpose |
|---|---|
| `algorithms/sorting.py` | 4 sorting implementations + comparison counts |
| `algorithms/fibonacci.py` | 3 Fibonacci implementations |
| `analysis/performance.py` | measurement harness (time, memory, datasets) |
| `analysis/visualizations.py` | matplotlib charts -> graphs/ |
| `notebook/run_analysis.py` | end-to-end pipeline (tables, CSVs, plots) |

## Report

Full write-up plus three submission pieces (experimental analysis,
complexity table, graphs): `Lab1_Aditya_Shibu_2401201047.pdf` (46 pp,
verified clean).
