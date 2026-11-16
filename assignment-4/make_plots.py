"""Draw the Lab 4 figures from real data into graphs/.

Six figures: runtime and memory scaling, three DP table heatmaps, and the
naive recursion against the DP table.
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from knapsack_dp import DEMO_CAPACITY, DEMO_ITEMS, knapsack_dp
from lcs import lcs_table
from matrix_chain import matrix_chain

BASE = Path(__file__).resolve().parent
GRAPHS = BASE / "graphs"
COLORS = {"LCS": "#2f6fb0", "0/1 Knapsack": "#2f8f5b", "Matrix Chain": "#b35c2f"}


def load_rows(name):
    rows = []
    with (BASE / "data" / name).open() as handle:
        for row in csv.DictReader(handle):
            rows.append({key: (float(value) if key in ("time_s", "memory_kb")
                               else int(value) if key in ("size", "calls", "subproblems")
                               else value)
                         for key, value in row.items()})
    return rows


def plot_metric(rows, key, ylabel, title, filename):
    grouped = {}
    for row in rows:
        grouped.setdefault(row["algorithm"], []).append((row["size"], row[key]))
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for name, points in grouped.items():
        points.sort()
        ax.plot([p[0] for p in points], [p[1] for p in points],
                marker="o", linewidth=2, label=name, color=COLORS[name])
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Problem size n")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPHS / filename, dpi=150)
    plt.close(fig)


def heatmap(matrix, row_labels, col_labels, title, filename, fmt="{:.0f}",
            xlabel="Column", ylabel="Row", height=4.8):
    values = np.array(matrix, dtype=float)
    fig, ax = plt.subplots(figsize=(8, height))
    image = ax.imshow(values, cmap="viridis")
    fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    ax.set_xticks(range(len(col_labels)), col_labels)
    ax.set_yticks(range(len(row_labels)), row_labels)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            if np.isfinite(values[i, j]):
                color = "white" if values[i, j] < values.max() * 0.6 else "black"
                ax.text(j, i, fmt.format(values[i, j]),
                        ha="center", va="center", fontsize=7, color=color)
    fig.tight_layout()
    fig.savefig(GRAPHS / filename, dpi=150)
    plt.close(fig)


def plot_lcs_heatmap():
    a, b = "AGGTAB", "GXTXAYB"
    table = lcs_table(a, b)
    heatmap(table, [""] + list(a), [""] + list(b),
            f"LCS table for {a} and {b} (length {table[-1][-1]})",
            "lcs_heatmap.png", xlabel="Second string b",
            ylabel="First string a")


def plot_knapsack_heatmap():
    items = DEMO_ITEMS
    capacity = DEMO_CAPACITY
    _, table, _ = knapsack_dp(items, capacity)
    rows = ["-"] + [name for name, _, _ in items]
    cols = [str(room) for room in range(capacity + 1)]
    heatmap(table, rows, cols,
            "0/1 knapsack table for the demo instance",
            "knapsack_heatmap.png", xlabel="Capacity",
            ylabel="Items considered", height=4.8)


def plot_mcm_heatmap():
    dims = [40, 20, 30, 10, 30]
    _, cost, _ = matrix_chain(dims)
    count = len(dims) - 1
    matrix = [[cost[i][j] if j >= i else np.nan for j in range(count)]
              for i in range(count)]
    labels = [f"M{i + 1}" for i in range(count)]
    heatmap(matrix, labels, labels,
            "Matrix chain cost table (dims 40, 20, 30, 10, 30)",
            "mcm_heatmap.png", xlabel="End matrix",
            ylabel="Start matrix", height=3.8)


def plot_recursive_compare():
    rows = load_rows("recursive_vs_dp.csv")
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for method, color in (("Naive recursion", "#b35c2f"), ("DP table", "#2f6fb0")):
        points = sorted((row["size"], row["time_s"]) for row in rows
                        if row["method"] == method)
        ax.plot([p[0] for p in points], [p[1] for p in points],
                marker="o", linewidth=2, label=method, color=color)
    ax.set_yscale("log")
    ax.set_xlabel("String length n")
    ax.set_ylabel("Median time (s)")
    ax.set_title("LCS: naive recursion vs DP table")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPHS / "recursive_vs_dp.png", dpi=150)
    plt.close(fig)


def main():
    GRAPHS.mkdir(parents=True, exist_ok=True)
    rows = load_rows("experiments.csv")
    plot_metric(rows, "time_s", "Median time (s)",
                "Execution time vs problem size", "runtime_dp.png")
    plot_metric(rows, "memory_kb", "Median peak memory (KB)",
                "Peak memory vs problem size", "memory_dp.png")
    plot_lcs_heatmap()
    plot_knapsack_heatmap()
    plot_mcm_heatmap()
    plot_recursive_compare()
    for path in sorted(GRAPHS.glob("*.png")):
        print(f"wrote {path.relative_to(BASE)}")


if __name__ == "__main__":
    main()
