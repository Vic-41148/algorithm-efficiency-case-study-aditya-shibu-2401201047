"""Longest Common Subsequence, bottom-up table plus naive recursion.

The DP table is (m+1) by (n+1). Each cell depends on the cell above, the
cell to the left, and the diagonal, so the run is O(mn) time and space.
The recursive version is kept to show the exponential cost without a table.
"""
import random


def lcs_table(a, b):
    """Return the (len(a)+1) by (len(b)+1) length table."""
    rows, cols = len(a) + 1, len(b) + 1
    table = [[0] * cols for _ in range(rows)]
    for i in range(1, rows):
        for j in range(1, cols):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table


def lcs_length(a, b):
    """Length of the longest common subsequence."""
    return lcs_table(a, b)[-1][-1]


def lcs_string(a, b):
    """Rebuild one longest common subsequence from the table."""
    table = lcs_table(a, b)
    i, j = len(a), len(b)
    output = []
    while i and j:
        if a[i - 1] == b[j - 1]:
            output.append(a[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] >= table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(output))


def lcs_recursive(a, b):
    """Naive recursion with no table. Returns (length, calls)."""
    calls = 0

    def walk(i, j):
        nonlocal calls
        calls += 1
        if i == 0 or j == 0:
            return 0
        if a[i - 1] == b[j - 1]:
            return 1 + walk(i - 1, j - 1)
        return max(walk(i - 1, j), walk(i, j - 1))

    return walk(len(a), len(b)), calls


def make_strings(n, seed=23, alphabet="ACGT"):
    """Two random strings of length n over the same alphabet."""
    rng = random.Random(seed)
    a = "".join(rng.choice(alphabet) for _ in range(n))
    b = "".join(rng.choice(alphabet) for _ in range(n))
    return a, b


if __name__ == "__main__":
    a, b = "AGGTAB", "GXTXAYB"
    table = lcs_table(a, b)
    print(f"a={a} b={b}")
    print(f"length={table[-1][-1]} string={lcs_string(a, b)}")
    for row in table:
        print(" ".join(f"{cell:2d}" for cell in row))
    length, calls = lcs_recursive(a, b)
    print(f"recursive length={length} calls={calls}")
