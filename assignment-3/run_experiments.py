"""Measure Fractional Knapsack, Activity Selection and Huffman Coding.

Writes data/experiments.csv with 5-run medians for time and peak memory.
Inputs are built before timing so only the algorithm is measured.
"""
import csv
import time
import tracemalloc
from pathlib import Path
from statistics import median

from activity_selection import activity_selection, make_activities
from fractional_knapsack import fractional_knapsack, make_items
from huffman_coding import build_codes, build_tree, make_frequencies

SIZES = [100, 200, 500, 1000, 2000, 5000, 10000]
REPEATS = 5
OUT = Path(__file__).resolve().parent / "data" / "experiments.csv"


def huffman_job(frequencies):
    """One full Huffman run: build the tree, then the code table."""
    return build_codes(build_tree(frequencies))


def time_and_memory(func, args, repeat=REPEATS):
    """Run func(*args) repeat times. Returns median seconds and median peak KB."""
    times, peaks = [], []
    for _ in range(repeat):
        tracemalloc.start()
        start = time.perf_counter()
        func(*args)
        times.append(time.perf_counter() - start)
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        peaks.append(peak / 1024)
    return median(times), median(peaks)


def build_cases():
    """Yield (algorithm, size, func, args) for every measured point."""
    for n in SIZES:
        items = make_items(n)
        capacity = sum(weight for _, _, weight in items) // 2
        yield "Fractional Knapsack", n, fractional_knapsack, (items, capacity)

        activities = make_activities(n)
        yield "Activity Selection", n, activity_selection, (activities,)

        frequencies = make_frequencies(n)
        yield "Huffman Coding", n, huffman_job, (frequencies,)


def main():
    rows = []
    for algorithm, n, func, args in build_cases():
        seconds, memory = time_and_memory(func, args)
        rows.append({"algorithm": algorithm, "size": n,
                     "time_s": f"{seconds:.6f}",
                     "memory_kb": f"{memory:.3f}"})
        print(f"{algorithm:20s} n={n:6d} time={seconds:.6f}s memory={memory:9.3f}KB")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["algorithm", "size", "time_s", "memory_kb"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"saved {OUT} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
