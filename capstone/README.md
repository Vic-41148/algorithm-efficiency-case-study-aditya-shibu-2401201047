# Capstone - Smart City Traffic Management and Route Optimization (ENCA351)

K.R. Mangalam University, School of Engineering and Technology.
Aditya Shibu (2401201047), BCA (AI & DS) Sec B. Faculty: Dr. Aarti.

Road network modeled as a weighted graph. Modules: Dijkstra route planning,
Bellman-Ford congestion analysis, BFS/DFS connectivity, Prim/Kruskal MST.

## Structure

```text
.
├── README.md
├── app.py                  # Streamlit app (4 module tabs)
├── route_planner.py        # graph model + Dijkstra
├── traffic_analysis.py     # Bellman-Ford + congestion compare
├── connectivity_module.py  # BFS + DFS
├── mst_planner.py          # Prim + Kruskal
├── run_experiments.py      # scaling runs -> data/experiments.csv
├── make_plots.py           # city map, MST map, scaling chart
├── project_notebook.ipynb  # demo notebook (executes clean)
├── requirements.txt
├── krmu_logo.png           # report front page
├── Aditya_Shibu_2401201047_ENCA351_Capstone_Traffic.md  # report source
├── Aditya_Shibu_2401201047_ENCA351_Capstone_Traffic.pdf # report (13 pp)
├── graphs/                 # city maps, scaling chart
├── data/                   # experiments.csv
└── screenshots/            # terminal evidence
```

## Run

```bash
python route_planner.py
python traffic_analysis.py
python connectivity_module.py
python mst_planner.py
python run_experiments.py
python make_plots.py
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
| `app.py` | interactive app (Tasks 2-7) |

## Report

Full write-up with module code, experiment tables, figures, analysis,
and conclusion:
`Aditya_Shibu_2401201047_ENCA351_Capstone_Traffic.pdf` (13 pp, verified clean).
