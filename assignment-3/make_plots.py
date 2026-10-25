"""Draw the Lab 3 figures from real data into graphs/.

Five figures: time scaling, memory scaling, activity timeline, Huffman tree,
and the fractional-knapsack allocation of one sample bag.
"""
import csv
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from activity_selection import activity_selection
from fractional_knapsack import fractional_knapsack
from huffman_coding import build_codes, build_tree

BASE = Path(__file__).resolve().parent
GRAPHS = BASE / "graphs"
DATA = BASE / "data" / "experiments.csv"
COLORS = {"Fractional Knapsack": "#2f6fb0",
          "Activity Selection": "#2f8f5b",
          "Huffman Coding": "#b35c2f"}


def load_rows():
    rows = []
    with DATA.open() as handle:
        for row in csv.DictReader(handle):
            rows.append({"algorithm": row["algorithm"],
                         "size": int(row["size"]),
                         "time_s": float(row["time_s"]),
                         "memory_kb": float(row["memory_kb"])})
    return rows


def series(rows, key):
    grouped = {}
    for row in rows:
        grouped.setdefault(row["algorithm"], []).append((row["size"], row[key]))
    return {name: sorted(points) for name, points in grouped.items()}


def plot_metric(rows, key, ylabel, title, filename):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for name, points in series(rows, key).items():
        xs = [point[0] for point in points]
        ys = [point[1] for point in points]
        ax.plot(xs, ys, marker="o", linewidth=2, label=name, color=COLORS[name])
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Input size n")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPHS / filename, dpi=150)
    plt.close(fig)


def plot_activity_timeline():
    activities = [
        ("A1", 1, 4), ("A2", 3, 5), ("A3", 0, 6), ("A4", 5, 7),
        ("A5", 3, 9), ("A6", 5, 9), ("A7", 6, 10), ("A8", 8, 11),
        ("A9", 8, 12), ("A10", 2, 14), ("A11", 12, 16),
    ]
    chosen = {activity[0] for activity in activity_selection(activities)}
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for index, (name, start, finish) in enumerate(activities):
        picked = name in chosen
        ax.barh(index, finish - start, left=start, height=0.6,
                color="#2f8f5b" if picked else "#d0d0d0",
                edgecolor="#204060" if picked else "#999999")
        ax.text(start + 0.2, index, f"{name} {start}-{finish}",
                va="center", fontsize=8)
    ax.set_yticks(range(len(activities)))
    ax.set_yticklabels([activity[0] for activity in activities])
    ax.invert_yaxis()
    ax.set_xlabel("Time")
    ax.set_title("Activity selection: chosen (green) vs rejected (gray)")
    ax.grid(axis="x", alpha=0.3)
    fig.tight_layout()
    fig.savefig(GRAPHS / "activity_timeline.png", dpi=150)
    plt.close(fig)


def plot_huffman_tree():
    text = "smart city traffic management"
    frequencies = Counter(text)
    root = build_tree(frequencies)
    codes = build_codes(root)

    positions = {}
    leaf_index = [0]

    def walk(node, depth):
        if node.is_leaf():
            x = leaf_index[0]
            leaf_index[0] += 1
            positions[id(node)] = (x, -depth)
            return x, -depth
        left = walk(node.left, depth + 1)
        right = walk(node.right, depth + 1)
        x = (left[0] + right[0]) / 2
        positions[id(node)] = (x, -depth)
        return x, -depth

    walk(root, 0)
    fig, ax = plt.subplots(figsize=(10, 5))
    stack = [root]
    while stack:
        node = stack.pop()
        x, y = positions[id(node)]
        if node.is_leaf():
            ax.scatter(x, y, s=220, color="#2f6fb0", zorder=3)
            ax.text(x, y + 0.25, f"{node.symbol!r}\n{node.weight}",
                    ha="center", va="bottom", fontsize=8)
        else:
            ax.scatter(x, y, s=120, color="#444444", zorder=3)
            ax.text(x, y + 0.2, str(node.weight), ha="center", va="bottom",
                    fontsize=7, color="#444444")
            for child in (node.left, node.right):
                cx, cy = positions[id(child)]
                ax.plot([x, cx], [y, cy], color="#888888", linewidth=1.2)
                stack.append(child)
    ax.set_title("Huffman tree for 'smart city traffic management'")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.margins(0.1)
    fig.tight_layout()
    fig.savefig(GRAPHS / "huffman_tree.png", dpi=150)
    plt.close(fig)


def plot_knapsack_allocation():
    items = [("A", 60, 10), ("B", 100, 20), ("C", 120, 30),
             ("D", 80, 15), ("E", 40, 8), ("F", 50, 12)]
    capacity = 60
    _, picks = fractional_knapsack(items, capacity)
    fractions = {name: 0.0 for name, _, _ in items}
    for name, fraction, _, _ in picks:
        fractions[name] = fraction
    ranked = sorted(items, key=lambda item: item[1] / item[2], reverse=True)
    names = [name for name, _, _ in ranked]
    values = [fractions[name] for name in names]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.barh(names, values, color="#2f6fb0")
    for bar, name in zip(bars, names):
        item = next(entry for entry in ranked if entry[0] == name)
        ratio = item[1] / item[2]
        taken = fractions[name]
        label = f"{taken * 100:.0f}% of {item[2]}kg, ratio {ratio:.2f}"
        if taken > 0.05:
            ax.text(0.02, bar.get_y() + bar.get_height() / 2, label,
                    va="center", fontsize=8, color="white")
        else:
            ax.text(0.02, bar.get_y() + bar.get_height() / 2, label + " (not reached)",
                    va="center", fontsize=8, color="#333333")
    ax.set_xlim(0, 1.05)
    ax.set_xlabel("Fraction taken")
    ax.set_title(f"Fractional knapsack allocation (capacity {capacity})")
    ax.invert_yaxis()
    fig.tight_layout()
    fig.savefig(GRAPHS / "knapsack_allocation.png", dpi=150)
    plt.close(fig)


def main():
    GRAPHS.mkdir(parents=True, exist_ok=True)
    rows = load_rows()
    plot_metric(rows, "time_s", "Median time (s)",
                "Execution time vs input size", "performance_time.png")
    plot_metric(rows, "memory_kb", "Median peak memory (KB)",
                "Peak memory vs input size", "performance_memory.png")
    plot_activity_timeline()
    plot_huffman_tree()
    plot_knapsack_allocation()
    for path in sorted(GRAPHS.glob("*.png")):
        print(f"wrote {path.relative_to(BASE)}")


if __name__ == "__main__":
    main()
