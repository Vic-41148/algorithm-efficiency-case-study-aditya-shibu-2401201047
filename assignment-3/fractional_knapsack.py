"""Fractional Knapsack: greedy by value/weight ratio, the last item may split.

Items are (name, value, weight) tuples. Sorting by ratio costs O(n log n);
the take pass is O(n), so the algorithm is O(n log n) time and O(n) space.
"""
import random


def fractional_knapsack(items, capacity):
    """Fill the bag by descending value/weight ratio.

    Returns (total_value, picks). picks holds
    (name, fraction, weight_taken, value_taken) in take order.
    """
    ranked = sorted(items, key=lambda item: item[1] / item[2], reverse=True)
    total_value = 0.0
    remaining = float(capacity)
    picks = []
    for name, value, weight in ranked:
        if remaining <= 0:
            break
        fraction = min(1.0, remaining / weight)
        used = weight * fraction
        gained = value * fraction
        picks.append((name, fraction, used, gained))
        total_value += gained
        remaining -= used
    return total_value, picks


def greedy_01(items, capacity):
    """Apply the same ratio rule to 0/1 knapsack: whole items only.

    Kept to show the failure case. It can miss the optimum because it never
    revisits an early choice.
    """
    ranked = sorted(items, key=lambda item: item[1] / item[2], reverse=True)
    total_value = 0
    remaining = capacity
    taken = []
    for name, value, weight in ranked:
        if weight <= remaining:
            taken.append(name)
            total_value += value
            remaining -= weight
    return total_value, taken


def knapsack_01_exact(items, capacity):
    """Exhaustive 0/1 optimum for small n. Returns (best_value, subset)."""
    best_value = 0
    best_subset = ()
    count = len(items)
    for mask in range(1 << count):
        weight = value = 0
        subset = []
        for i in range(count):
            if mask & (1 << i):
                subset.append(items[i][0])
                value += items[i][1]
                weight += items[i][2]
        if weight <= capacity and value > best_value:
            best_value = value
            best_subset = tuple(subset)
    return best_value, best_subset


def make_items(n, seed=7):
    """Random items with value and weight in 1..100."""
    rng = random.Random(seed)
    return [(f"item{i:05d}", rng.randint(1, 100), rng.randint(1, 100))
            for i in range(n)]


if __name__ == "__main__":
    sample = [("gold", 60, 10), ("silver", 100, 20), ("bronze", 120, 30)]
    capacity = 50
    value, picks = fractional_knapsack(sample, capacity)
    print(f"capacity={capacity} items={len(sample)}")
    for name, fraction, used, gained in picks:
        print(f"{name:7s} take={fraction:4.2f} weight={used:5.1f} value={gained:7.2f}")
    print(f"total value={value:.2f}")

    counterexample = [("C", 10, 6), ("A", 6, 5), ("B", 5, 5)]
    bag = 10
    greedy_value, greedy_items = greedy_01(counterexample, bag)
    exact_value, exact_items = knapsack_01_exact(counterexample, bag)
    print(f"0/1 greedy={greedy_value} {greedy_items}")
    print(f"0/1 exact ={exact_value} {exact_items}")
