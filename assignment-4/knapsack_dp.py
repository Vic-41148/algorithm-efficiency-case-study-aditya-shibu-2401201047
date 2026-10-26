"""0/1 Knapsack, bottom-up table plus a one-row space optimisation.

Items are (name, value, weight) tuples. The table is (n+1) by (capacity+1),
so the run is O(n * capacity) time and space. The one-row version keeps
O(capacity) space by scanning the capacity backwards.
"""
import random


def knapsack_dp(items, capacity):
    """Return (best_value, table, chosen) for whole-item knapsack."""
    count = len(items)
    table = [[0] * (capacity + 1) for _ in range(count + 1)]
    for i in range(1, count + 1):
        _, value, weight = items[i - 1]
        for room in range(capacity + 1):
            table[i][room] = table[i - 1][room]
            if weight <= room:
                table[i][room] = max(table[i][room],
                                     table[i - 1][room - weight] + value)
    chosen = []
    room = capacity
    for i in range(count, 0, -1):
        if table[i][room] != table[i - 1][room]:
            name = items[i - 1][0]
            chosen.append(name)
            room -= items[i - 1][2]
    return table[count][capacity], table, list(reversed(chosen))


def knapsack_1d(items, capacity):
    """Same answer with one row of state. Returns the best value only."""
    best = [0] * (capacity + 1)
    for _, value, weight in items:
        for room in range(capacity, weight - 1, -1):
            if best[room - weight] + value > best[room]:
                best[room] = best[room - weight] + value
    return best[capacity]


def make_items(n, seed=29, max_value=100, max_weight=100):
    """Random items with value and weight in 1..max."""
    rng = random.Random(seed)
    return [(f"item{i:04d}", rng.randint(1, max_value),
             rng.randint(1, max_weight)) for i in range(n)]


if __name__ == "__main__":
    items = [("map", 10, 5), ("compass", 40, 4), ("water", 30, 6),
             ("tent", 50, 9), ("food", 35, 5), ("radio", 25, 3)]
    capacity = 15
    best, table, chosen = knapsack_dp(items, capacity)
    print(f"capacity={capacity} items={len(items)}")
    print(f"best value={best} chosen={chosen}")
    print(f"one-row check={knapsack_1d(items, capacity)}")
    print(f"table rows={len(table)} cols={len(table[0])}")
