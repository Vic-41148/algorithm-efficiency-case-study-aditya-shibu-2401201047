"""Small interactive menu for the three Lab 4 dynamic programs."""
from knapsack_dp import DEMO_CAPACITY, DEMO_ITEMS, knapsack_1d, knapsack_dp
from lcs import lcs_recursive, lcs_string, lcs_table
from matrix_chain import matrix_chain, parenthesize


def run_lcs():
    a = input("First string [AGGTAB]: ").strip() or "AGGTAB"
    b = input("Second string [GXTXAYB]: ").strip() or "GXTXAYB"
    table = lcs_table(a, b)
    print(f"length={table[-1][-1]} string={lcs_string(a, b)}")
    if max(len(a), len(b)) <= 20:
        _, calls = lcs_recursive(a, b)
        print(f"recursive_calls={calls}")
    else:
        print("naive recursion skipped above length 20")
    print("table:")
    for row in table:
        print(" ".join(f"{cell:2d}" for cell in row))


def run_knapsack():
    print(f"demo items={DEMO_ITEMS}")
    raw = input(f"Capacity [{DEMO_CAPACITY}]: ").strip()
    try:
        capacity = int(raw) if raw else DEMO_CAPACITY
    except ValueError:
        print("Capacity must be an integer")
        return
    if capacity < 0:
        print("Capacity must be zero or more")
        return
    best, table, chosen = knapsack_dp(DEMO_ITEMS, capacity)
    print(f"best value={best} chosen={chosen}")
    print(f"one-row check={knapsack_1d(DEMO_ITEMS, capacity)}")
    print("table:")
    for row in table:
        print(" ".join(f"{cell:4d}" for cell in row))


def run_matrix_chain():
    raw = input("Dimensions [40 20 30 10 30]: ").strip()
    try:
        dims = [int(part) for part in (raw or "40 20 30 10 30").split()]
    except ValueError:
        print("Dimensions must be integers")
        return
    if len(dims) < 2:
        print("Need at least two dimensions")
        return
    best, _, split = matrix_chain(dims)
    print(f"min cost={best} order={parenthesize(split, 0, len(dims) - 2)}")
    print("split table:")
    for row in split:
        print(" ".join(f"{cell:2d}" for cell in row))


def main():
    while True:
        print("\n1 LCS\n2 0/1 Knapsack\n3 Matrix Chain\n4 Quit")
        choice = input("Choice: ").strip().lower()
        if choice == "1":
            run_lcs()
        elif choice == "2":
            run_knapsack()
        elif choice == "3":
            run_matrix_chain()
        elif choice in ("4", "q", "quit"):
            print("Bye")
            return
        else:
            print("Choose 1 to 4")


if __name__ == "__main__":
    main()
