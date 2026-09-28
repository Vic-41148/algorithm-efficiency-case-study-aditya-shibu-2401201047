import sys
# run from this folder: plain local imports
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from route_planner import build_sample_city, dijkstra
from mst_planner import prim
import csv

city, coords = build_sample_city()
path, cost, _ = dijkstra(city, "Library", "Airport")
path_edges = {tuple(sorted(e)) for e in zip(path, path[1:])}
pe, pt = prim(city)
mst_edges = {tuple(sorted((u, v))) for u, v, _ in pe}

def draw(highlight, title, out):
    plt.figure(figsize=(9, 6))
    for u, v, w in city.roads():
        x = [coords[u][0], coords[v][0]]
        y = [coords[u][1], coords[v][1]]
        hot = tuple(sorted((u, v))) in highlight
        plt.plot(x, y, color="red" if hot else "0.75",
                 linewidth=3 if hot else 1.5, zorder=1)
        plt.text(sum(x)/2, sum(y)/2, str(w), fontsize=9,
                 color="red" if hot else "0.4", zorder=3)
    for n, (x, y) in coords.items():
        plt.scatter([x], [y], s=260, c="steelblue", zorder=2)
        plt.text(x, y + 0.28, n, fontsize=9, ha="center", weight="bold")
    plt.title(title)
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.close()
    print("saved", out)

G = "graphs/"
draw(path_edges, f"Library -> Airport shortest path (cost {cost})", G + "city_shortest_path.png")
draw(mst_edges, f"Minimum spanning tree (total {pt})", G + "city_mst.png")

rows = list(csv.DictReader(open("data/experiments.csv")))
sizes = sorted({int(r["size"]) for r in rows})
plt.figure(figsize=(9, 5))
for algo in ("BFS", "DFS", "Dijkstra", "Bellman-Ford", "Prim", "Kruskal"):
    ts = [float(next(r["time_s"] for r in rows if int(r["size"]) == n and r["algo"] == algo)) for n in sizes]
    plt.plot(sizes, ts, marker="o", label=algo)
plt.xlabel("Intersections (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Scaling: all algorithms vs network size")
plt.legend()
plt.grid(True)
plt.savefig(G + "scaling.png", dpi=150)
plt.close()
print("saved", G + "scaling.png")
