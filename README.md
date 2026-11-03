# Design and Analysis of Algorithms Lab (ENCA301 / ENCA351)

K.R. Mangalam University, Aditya Shibu (2401201047), BCA (AI & DS) Sec B.
Submitted to Dr. Aarti Sangwan.

One folder per assignment. Every assignment folder is flat: code plus
report source (`.md`), submission PDF, `screenshots/`, `graphs/`, and
its own `README.md`.

## Structure

```text
.
├── README.md
├── LICENSE
├── requirements.txt      # shared env (venv/ is ignored)
├── assignment-1/         # Lab 1: sorting + Fibonacci efficiency, done
│   ├── README.md requirements.txt
│   ├── algorithms/ analysis/ notebook/ graphs/ data/ screenshots/
│   ├── image-57.png (report logo)
│   └── Lab1_Aditya_Shibu_2401201047.md/.pdf + 3 submission pieces
├── assignment-2/         # Lab 2: benchmarking tool, done
│   ├── README.md requirements.txt
│   ├── app.py search_analysis.py code_benchmark.py benchmark_engine.py
│   ├── run_full_sweep.py visualize.py project_notebook.ipynb
│   ├── Aditya_Shibu_2401201047_ENCA351_Lab2_Benchmark.md/.pdf (11 pp)
│   └── graphs/ data/ screenshots/
├── assignment-3/         # Lab 3: smart allocation and scheduling, done
│   ├── README.md requirements.txt
│   ├── fractional_knapsack.py activity_selection.py huffman_coding.py
│   ├── run_experiments.py make_plots.py
│   ├── Aditya_Shibu_2401201047_ENCA351_Lab3.md/.pdf (20 pp)
│   ├── Lab3_Performance_Complexity_...pdf (4 pp), Lab3_Graphs_Visualizations_...pdf (5 pp)
│   └── graphs/ data/ screenshots/
├── assignment-4/         # Lab 4: dynamic programming, done
│   ├── README.md requirements.txt
│   ├── lcs.py knapsack_dp.py matrix_chain.py
│   ├── run_experiments.py make_plots.py
│   ├── Aditya_Shibu_2401201047_ENCA351_Lab4.md/.pdf (18 pp)
│   ├── Lab4_Performance_Complexity_...pdf (5 pp), Lab4_Graphs_Visualizations_...pdf (5 pp)
│   └── graphs/ data/ screenshots/
└── capstone/             # Smart City Traffic, done
    ├── README.md requirements.txt
    ├── app.py route_planner.py traffic_analysis.py connectivity_module.py
    ├── mst_planner.py run_experiments.py run_scenarios.py tests.py
    ├── make_plots.py sample_roads.csv project_notebook.ipynb
    ├── Aditya_Shibu_2401201047_ENCA351_Capstone_Traffic.md/.pdf (25 pp)
    └── graphs/ data/ screenshots/
```

Every assignment folder is flat with the same contract: code plus report
source (`.md`), submission PDF, `screenshots/`, `graphs/`, `data/` where
used, and its own `README.md` + `requirements.txt`.

## Reports

| Assignment | PDF | Pages |
|---|---|---|
| Lab 1 | `assignment-1/Lab1_Aditya_Shibu_2401201047.pdf` (+ complexity, experimental-analysis, graphs pieces) | 46 |
| Lab 2 | `assignment-2/Aditya_Shibu_2401201047_ENCA351_Lab2_Benchmark.pdf` | 11 |
| Lab 3 | `assignment-3/Aditya_Shibu_2401201047_ENCA351_Lab3.pdf` (+ performance-complexity 4 pp, visualizations 5 pp) | 20 |
| Lab 4 | `assignment-4/Aditya_Shibu_2401201047_ENCA351_Lab4.pdf` (+ performance-complexity 5 pp, visualizations 5 pp) | 18 |
| Capstone | `capstone/Aditya_Shibu_2401201047_ENCA351_Capstone_Traffic.pdf` | 25 |

All PDFs verify clean (ASSIGN-MAKER `tools/verify_pdf.py`: zero blank/short
pages) and were checked page by page against the Lab 1 reference formatting.

## Run

```bash
cd assignment-2 && python run_full_sweep.py all   # Lab 2 numbers
cd ../assignment-3 && python run_experiments.py   # Lab 3 numbers
cd ../assignment-4 && python run_experiments.py   # Lab 4 numbers
cd ../capstone && python run_experiments.py       # capstone numbers
```
