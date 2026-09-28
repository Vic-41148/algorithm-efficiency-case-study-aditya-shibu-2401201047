import time, random, tracemalloc
# run from this folder: plain local imports
from route_planner import RoadNetwork, dijkstra
from traffic_analysis import bellman_ford
from connectivity_module import bfs, dfs
from mst_planner import prim, kruskal

def random_city(n, seed=7):
    rnd = random.Random(seed)
    g = RoadNetwork()
    names = [f"N{i}" for i in range(n)]
    for i in range(1, n):
        g.add_road(names[i], names[rnd.randrange(i)], rnd.randint(1, 20))
    for _ in range(n // 2):
        u, v = rnd.sample(names, 2)
        if v not in g.adj[u]:
            g.add_road(u, v, rnd.randint(1, 20))
    return g, names

def timed(func, *args, runs=5):
    ts, ms = [], []
    for _ in range(runs):
        tracemalloc.start()
        t = time.perf_counter()
        out = func(*args)
        dt = time.perf_counter() - t
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        ts.append(dt); ms.append(peak / 1024)
    return out, min(ts), min(ms)

print("size,roads,algo,time_s,mem_kb,extra")
rows = []
for n in (10, 25, 50, 100):
    g, names = random_city(n)
    m = len(g.roads())
    (_, _), tb, mb = timed(bfs, g, "N0")
    (_, _), td, md = timed(dfs, g, "N0")
    (p, c, _), tj, mj = timed(dijkstra, g, "N0", f"N{n-1}")
    (d, pr, tr, ok), tb2, mb2 = timed(bellman_ford, g, "N0")
    (pe, pt), tp, mp = timed(prim, g)
    (ke, kt), tk, mk = timed(kruskal, g)
    assert pt == kt, "MST totals disagree"
    assert c == d[f"N{n-1}"], "Dijkstra/BF disagree"
    for algo, t, mm, ex in (("BFS", tb, mb, "-"), ("DFS", td, md, "-"),
                            ("Dijkstra", tj, mj, f"cost={c}"),
                            ("Bellman-Ford", tb2, mb2, f"cost={d[f'N{n-1}']}"),
                            ("Prim", tp, mp, f"mst={pt}"),
                            ("Kruskal", tk, mk, f"mst={kt}")):
        print(f"{n},{m},{algo},{t:.6f},{mm:.2f},{ex}")
        rows.append((n, m, algo, t, mm, ex))
import csv
with open("data/experiments.csv", "w") as f:
    w = csv.writer(f)
    w.writerow(["size", "roads", "algo", "time_s", "mem_kb", "extra"])
    w.writerows(rows)
print("saved experiments.csv")
