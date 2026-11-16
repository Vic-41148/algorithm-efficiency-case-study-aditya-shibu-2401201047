"""Matrix Chain Multiplication, interval DP.

dims has n+1 entries for n matrices. The table is n by n and every entry
cost[i][j] is the cheapest cost to multiply matrices i..j. Each entry tries
every split point, so the run is O(n^3) time and O(n^2) space.
"""
import random


def matrix_chain(dims):
    """Return (min_cost, cost_table, split_table) for the given dimensions."""
    count = len(dims) - 1
    cost = [[0] * count for _ in range(count)]
    split = [[0] * count for _ in range(count)]
    for length in range(2, count + 1):
        for i in range(count - length + 1):
            j = i + length - 1
            cost[i][j] = float("inf")
            for k in range(i, j):
                candidate = (cost[i][k] + cost[k + 1][j]
                             + dims[i] * dims[k + 1] * dims[j + 1])
                if candidate < cost[i][j]:
                    cost[i][j] = candidate
                    split[i][j] = k
    return cost[0][count - 1], cost, split


def parenthesize(split, i, j):
    """Rebuild the optimal grouping from the split table."""
    if i == j:
        return f"M{i + 1}"
    k = split[i][j]
    return "(" + parenthesize(split, i, k) + " x " + parenthesize(split, k + 1, j) + ")"


def make_dims(n, seed=31, low=10, high=100):
    """n+1 random dimensions for n matrices."""
    rng = random.Random(seed)
    return [rng.randint(low, high) for _ in range(n + 1)]


if __name__ == "__main__":
    dims = [40, 20, 30, 10, 30]
    best, cost, split = matrix_chain(dims)
    print(f"dims={dims}")
    print(f"matrices={len(dims) - 1} min cost={best}")
    print(f"order={parenthesize(split, 0, len(dims) - 2)}")
    print("cost table:")
    for row in cost:
        print(" ".join(f"{cell:8.0f}" for cell in row))
    print("split table (0-indexed k):")
    for row in split:
        print(" ".join(f"{cell:2d}" for cell in row))
