# Design and Analysis of Algorithms Lab (ENCA301 / ENCA351)

K.R. Mangalam University — Aditya Shibu (2401201047), BCA (AI & DS) Sec B.
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
├── assignment-1/         # Lab 1: sorting + Fibonacci efficiency — done
│   ├── README.md requirements.txt
│   ├── algorithms/ analysis/ notebook/ graphs/ data/ screenshots/
│   ├── image-57.png (report logo)
│   └── Lab1_Aditya_Shibu_2401201047.md/.pdf + 3 submission pieces
├── assignment-2/         # Lab 2: benchmarking tool — done
│   ├── README.md requirements.txt
│   ├── app.py search_analysis.py code_benchmark.py benchmark_engine.py
│   ├── run_full_sweep.py visualize.py project_notebook.ipynb
│   ├── Aditya_Shibu_2401201047_ENCA351_Lab2_Benchmark.md/.pdf (11 pp)
│   └── graphs/ data/ screenshots/
└── capstone/             # Smart City Traffic — done
    ├── README.md requirements.txt
    ├── app.py route_planner.py traffic_analysis.py connectivity_module.py
    ├── mst_planner.py run_experiments.py make_plots.py project_notebook.ipynb
    ├── Aditya_Shibu_2401201047_ENCA351_Capstone_Traffic.md/.pdf (17 pp)
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
| Capstone | `capstone/Aditya_Shibu_2401201047_ENCA351_Capstone_Traffic.pdf` | 17 |

All PDFs verify clean (ASSIGN-MAKER `tools/verify_pdf.py`: zero blank/short
pages) and were checked page by page against the Lab 1 reference formatting.

## Run

```bash
cd assignment-2 && python run_full_sweep.py all   # Lab 2 numbers
cd ../capstone && python run_experiments.py       # capstone numbers
```
