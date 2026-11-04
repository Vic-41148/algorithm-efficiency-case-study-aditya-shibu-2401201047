# Capstone - Smart City Traffic Management and Route Optimization (ENCA351)

K.R. Mangalam University, School of Engineering and Technology.
Aditya Shibu (2401201047), BCA (AI & DS) Sec B. Faculty: Dr. Aarti Sangwan.

Road network modeled as a weighted graph. Modules: Dijkstra route planning,
Bellman-Ford congestion analysis, BFS/DFS connectivity, Prim/Kruskal MST.

## Structure

```text
.
├── README.md
├── app.py                  # Streamlit app (4 module tabs)
├── route_planner.py        # graph model + Dijkstra
├── traffic_analysis.py     # Bellman-Ford + congestion compare
├── connectivity_module.py  # BFS + DFS, returns tree edges
├── mst_planner.py          # Prim + Kruskal
├── run_experiments.py      # scaling runs -> data/experiments.csv
├── run_scenarios.py        # congestion cases -> data/congestion_scenarios.csv
├── tests.py                # 10 unittest cases
├── make_plots.py           # city map, trees, congestion, scaling chart
├── sample_roads.csv        # CSV network (10 nodes, 14 roads)
├── project_notebook.ipynb  # demo notebook (executes clean)
├── requirements.txt
├── krmu_logo.png           # report front page
├── Aditya_Shibu_2401201047_ENCA351_Capstone_Traffic.md  # report source
├── Aditya_Shibu_2401201047_ENCA351_Capstone_Traffic.pdf # report (25 pp)
├── graphs/                 # city maps, BFS/DFS trees, congestion, scaling
├── data/                   # experiments.csv, congestion_scenarios.csv
└── screenshots/            # terminal runs, matrix, tests, app tabs
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python route_planner.py
python traffic_analysis.py
python connectivity_module.py
python mst_planner.py
python run_experiments.py
python run_scenarios.py
python make_plots.py
python -m unittest -v
streamlit run app.py
```

## Module map

| File | Brief task |
|---|---|
| `route_planner.py` | Task 3 modeling + Task 4 Dijkstra routing |
| `traffic_analysis.py` | Task 5 congestion analysis (Bellman-Ford) |
| `connectivity_module.py` | Task 6 BFS/DFS connectivity |
| `mst_planner.py` | Task 7 Prim/Kruskal infrastructure |
| `run_experiments.py` + `make_plots.py` | Task 8 scaling runs + Task 9 figures |
| `run_scenarios.py` + `tests.py` | congestion scenarios + 10 contract tests |
| `app.py` | interactive app (Tasks 2-7) |

## Report

Full write-up with module code, experiment tables, figures, analysis,
and conclusion:
`Aditya_Shibu_2401201047_ENCA351_Capstone_Traffic.pdf` (25 pp, 17 images,
verified clean).

## Verification

Build and check the report from this folder:

```bash
python3 /home/vic/Projects/ASSIGN-MAKER/tools/pipeline.py \
  Aditya_Shibu_2401201047_ENCA351_Capstone_Traffic.md --require-github
```

Run the contract tests:

```bash
python3 -m unittest -v
```

Data provenance:

- `data/experiments.csv` comes from `run_experiments.py` (10 to 200 nodes,
  timing best of 25 runs, memory median of 7 traced runs).
- `data/congestion_scenarios.csv` comes from `run_scenarios.py`.
- Report tables come from those CSV files; figures come from
  `make_plots.py`.

`run_experiments.py` and `run_scenarios.py` are import-safe; their `main()`
runs only under `if __name__ == "__main__":`.
