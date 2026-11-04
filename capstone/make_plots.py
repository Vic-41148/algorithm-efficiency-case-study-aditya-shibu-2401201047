import sys
# run from this folder: plain local imports
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from route_planner import build_sample_city, dijkstra
from traffic_analysis import compare_routes
from connectivity_module import bfs, dfs
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
    plt.title(title, pad=15)
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.close()
    print("saved", out)

G = "graphs/"
draw(path_edges, f"Library -> Airport shortest path (cost {cost})", G + "city_shortest_path.png")
draw(mst_edges, f"Minimum spanning tree (total {pt})", G + "city_mst.png")


def draw_tree(tree, order, title, out, color):
    visit = {n: i + 1 for i, n in enumerate(order)}
    plt.figure(figsize=(9, 6))
    for u, v, w in city.roads():
        x = [coords[u][0], coords[v][0]]
        y = [coords[u][1], coords[v][1]]
        plt.plot(x, y, color="0.85", linewidth=1.2, zorder=1)
        plt.text(sum(x) / 2, sum(y) / 2, str(w), fontsize=8,
                 color="0.6", zorder=2)
    for u, v in tree:
        plt.annotate("", xy=coords[v], xytext=coords[u],
                     arrowprops=dict(arrowstyle="-|>", color=color, lw=2.4,
                                     shrinkA=12, shrinkB=12), zorder=3)
    for n, (x, y) in coords.items():
        plt.scatter([x], [y], s=300, c="white", edgecolors=color,
                    linewidths=2, zorder=4)
        plt.text(x, y + 0.32, f"{n} (#{visit[n]})", fontsize=9,
                 ha="center", weight="bold", zorder=5)
    plt.title(title, pad=15)
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.close()
    print("saved", out)


def draw_congestion(result, jammed, factor, out):
    jam_set = {tuple(sorted(e)) for e in jammed}
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.8))
    panels = (("original", "Original route"),
              ("congested", f"After jams (weight x{factor})"))
    for ax, (key, label) in zip(axes, panels):
        path, cost = result[key]
        route = {tuple(sorted(e)) for e in zip(path, path[1:])}
        for u, v, w in city.roads():
            x = [coords[u][0], coords[v][0]]
            y = [coords[u][1], coords[v][1]]
            edge = tuple(sorted((u, v)))
            if edge in jam_set:
                ax.plot(x, y, color="orange", linewidth=4,
                        linestyle="--", zorder=1)
                ax.text(sum(x) / 2, sum(y) / 2 - 0.28, f"{w} x{factor}",
                        fontsize=8, color="darkorange", ha="center", zorder=4)
            else:
                ax.plot(x, y, color="0.8", linewidth=1.4, zorder=1)
                ax.text(sum(x) / 2, sum(y) / 2, str(w), fontsize=8,
                        color="0.55", zorder=2)
            if edge in route:
                ax.plot(x, y, color="tab:blue", linewidth=3, zorder=2)
        for n, (x, y) in coords.items():
            ax.scatter([x], [y], s=240, c="white", edgecolors="tab:blue",
                       linewidths=1.5, zorder=5)
            ax.text(x, y + 0.3, n, fontsize=8.5, ha="center",
                    weight="bold", zorder=6)
        ax.set_title(f"{label}: cost {cost}", pad=12)
        ax.axis("equal")
        ax.axis("off")
    fig.text(0.5, 0.02, f"Orange dashed: jammed roads, weight x{factor}. "
             "Blue: chosen route.", ha="center", fontsize=9, color="0.3")
    plt.tight_layout(rect=(0, 0.05, 1, 1))
    plt.savefig(out, dpi=150)
    plt.close()
    print("saved", out)


b_order, _, b_tree = bfs(city, "Library")
d_order, _, d_tree = dfs(city, "Library")
draw_tree(b_tree, b_order, "BFS tree from Library (visit order #n)",
          G + "bfs_tree.png", "tab:green")
draw_tree(d_tree, d_order, "DFS tree from Library (visit order #n)",
          G + "dfs_tree.png", "tab:purple")

jam_edges = [("Market", "Mall"), ("Mall", "Airport")]
jam_result = compare_routes(city, "Library", "Airport", jam_edges, 3)
draw_congestion(jam_result, jam_edges, 3, G + "congestion_reroute.png")


rows = list(csv.DictReader(open("data/experiments.csv")))
sizes = sorted({int(r["size"]) for r in rows})
plt.figure(figsize=(9, 5))
for algo in ("BFS", "DFS", "Dijkstra", "Bellman-Ford", "Prim", "Kruskal"):
    ts = [float(next(r["time_s"] for r in rows if int(r["size"]) == n and r["algo"] == algo)) for n in sizes]
    plt.plot(sizes, ts, marker="o", label=algo)
plt.xlabel("Intersections (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Scaling: all algorithms vs network size", pad=12)
plt.legend()
plt.grid(True)
plt.savefig(G + "scaling.png", dpi=150)
plt.close()
print("saved", G + "scaling.png")
