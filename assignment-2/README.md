# Lab 2 - Algorithm Performance Measurement and Benchmarking Tool (ENCA351)

K.R. Mangalam University, School of Engineering and Technology.
Aditya Shibu (2401201047), BCA (AI & DS) Sec B. Faculty: Dr. Aarti Sangwan.

A reusable benchmarking tool (time via `time.perf_counter`, memory via
`tracemalloc`) applied to Linear/Binary Search and four code patterns
(single loop, nested loop, recursive/iterative factorial).

## Structure

```text
.
├── README.md
├── app.py                  # Streamlit interactive app
├── search_analysis.py      # Q2: Linear + Binary Search
├── code_benchmark.py       # Q3: loop + factorial patterns
├── benchmark_engine.py     # Q4: automated engine (any func, any sizes)
├── run_full_sweep.py       # brief-size sweep -> data/sweep_full.csv
├── visualize.py            # Q6: time + memory charts -> graphs/
├── project_notebook.ipynb  # demo notebook (executes clean)
├── requirements.txt
├── krmu_logo.png           # report front page
├── Aditya_Shibu_2401201047_ENCA351_Lab2_Benchmark.md  # report source
├── Aditya_Shibu_2401201047_ENCA351_Lab2_Benchmark.pdf # report (11 pp)
├── graphs/                 # sweep_time.png, sweep_memory.png
├── data/                   # sweep_full.csv (30 rows)
└── screenshots/            # terminal evidence
```

## Run

```bash
python search_analysis.py
python code_benchmark.py
python benchmark_engine.py     # prints table, saves benchmark_results.csv
python run_full_sweep.py all   # brief sizes incl. nested-50k
python visualize.py
streamlit run app.py
```

## Module map

| File | Brief task |
|---|---|
| `search_analysis.py` | Q2 search lab |
| `code_benchmark.py` | Q3 snippet lab |
| `benchmark_engine.py` | Q4 auto engine |
| `run_full_sweep.py` | Q4 brief-size sweep |
| `visualize.py` | Q6 charts |
| `app.py` | interactive app (Q2-Q6) |

## Report

Full write-up with result tables, charts, analysis, and conclusion:
`Aditya_Shibu_2401201047_ENCA351_Lab2_Benchmark.pdf` (11 pp, verified clean).
