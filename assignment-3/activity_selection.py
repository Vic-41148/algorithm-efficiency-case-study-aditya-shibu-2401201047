"""Activity Selection: keep the largest set of non-overlapping activities.

Activities are (name, start, finish) tuples. Sorting by finish time costs
O(n log n); the selection pass is O(n), so O(n log n) time and O(n) space.
"""
import random


def activity_selection(activities):
    """Pick every activity that starts after the last chosen one finishes.

    Returns the selected (name, start, finish) tuples in finish order.
    """
    ranked = sorted(activities, key=lambda act: act[2])
    selected = []
    last_finish = float("-inf")
    for activity in ranked:
        name, start, finish = activity
        if start >= last_finish:
            selected.append(activity)
            last_finish = finish
    return selected


def make_activities(n, horizon=10000, seed=11):
    """Random activities with start in 0..horizon and length in 1..100."""
    rng = random.Random(seed)
    activities = []
    for i in range(n):
        start = rng.randint(0, horizon)
        finish = start + rng.randint(1, 100)
        activities.append((f"act{i:05d}", start, finish))
    return activities


if __name__ == "__main__":
    sample = [
        ("A1", 1, 4),
        ("A2", 3, 5),
        ("A3", 0, 6),
        ("A4", 5, 7),
        ("A5", 3, 9),
        ("A6", 5, 9),
        ("A7", 6, 10),
        ("A8", 8, 11),
        ("A9", 8, 12),
        ("A10", 2, 14),
        ("A11", 12, 16),
    ]
    chosen = activity_selection(sample)
    print(f"activities={len(sample)} selected={len(chosen)}")
    for name, start, finish in chosen:
        print(f"{name:4s} start={start:3d} finish={finish:3d}")
