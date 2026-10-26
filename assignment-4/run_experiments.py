"""Measure LCS, 0/1 Knapsack and Matrix Chain Multiplication.

Writes data/experiments.csv (time, peak memory, subproblem count) and
data/recursive_vs_dp.csv (naive LCS recursion against the DP table).
"""
import csv
import time
import tracemalloc
from pathlib import Path
from statistics import median

from knapsack_dp import knapsack_dp, make_items
from lcs import lcs_recursive, lcs_table, make_strings
from matrix_chain import make_dims, matrix_chain

LCS_SIZES = [50, 100, 200, 400, 800, 1200]
KNAPSACK_SIZES = [50, 100, 200, 400, 800]
MATRIX_SIZES = [10, 20, 40, 80, 120, 160]
RECURSIVE_SIZES = [6, 8, 10, 12, 14, 16]
REPEATS = 5
BASE = Path(__file__).resolve().parent


def time_and_memory(func, args, repeat=REPEATS):
    """Median wall time (timing runs) and median peak KB (traced runs).

    Timing runs keep tracemalloc off, so the clock is not inflated by
    allocation tracking on the large tables. Memory comes from separate runs.
    """
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        func(*args)
        times.append(time.perf_counter() - start)

    peaks = []
    for _ in range(3):
        tracemalloc.start()
        func(*args)
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        peaks.append(peak / 1024)
    return median(times), median(peaks)


def dp_cases():
    """Yield (algorithm, size, func, args, subproblems) for the DP sweep."""
    for n in LCS_SIZES:
        a, b = make_strings(n)
        yield "LCS", n, lcs_table, (a, b), n * n

    for n in KNAPSACK_SIZES:
        items = make_items(n)
        capacity = 2 * n
        yield "0/1 Knapsack", n, knapsack_dp, (items, capacity), n * capacity

    for n in MATRIX_SIZES:
        dims = make_dims(n)
        yield "Matrix Chain", n, matrix_chain, (dims,), n * (n + 1) // 2


def run_dp_sweep():
    rows = []
    for algorithm, n, func, args, subproblems in dp_cases():
        seconds, memory = time_and_memory(func, args)
        rows.append({"algorithm": algorithm, "size": n,
                     "time_s": f"{seconds:.6f}",
                     "memory_kb": f"{memory:.3f}",
                     "subproblems": subproblems})
        print(f"{algorithm:14s} n={n:5d} time={seconds:.6f}s "
              f"memory={memory:10.3f}KB cells={subproblems}")
    return rows


def run_recursive_compare():
    rows = []
    for n in RECURSIVE_SIZES:
        a, b = make_strings(n, seed=37)
        tracemalloc.start()
        start = time.perf_counter()
        _, calls = lcs_recursive(a, b)
        seconds = time.perf_counter() - start
        tracemalloc.stop()
        rows.append({"size": n, "method": "Naive recursion",
                     "time_s": f"{seconds:.6f}", "calls": calls})
        dp_seconds, _ = time_and_memory(lcs_table, (a, b))
        rows.append({"size": n, "method": "DP table",
                     "time_s": f"{dp_seconds:.6f}", "calls": n * n})
        print(f"n={n:2d} recursion={rows[-2]['time_s']}s calls={calls:,} "
              f"dp={rows[-1]['time_s']}s")
    return rows


def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"saved {path} ({len(rows)} rows)")


def main():
    dp_rows = run_dp_sweep()
    write_csv(BASE / "data" / "experiments.csv", dp_rows,
              ["algorithm", "size", "time_s", "memory_kb", "subproblems"])
    recursion_rows = run_recursive_compare()
    write_csv(BASE / "data" / "recursive_vs_dp.csv", recursion_rows,
              ["size", "method", "time_s", "calls"])


if __name__ == "__main__":
    main()
