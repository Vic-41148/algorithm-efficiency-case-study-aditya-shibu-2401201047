"""Huffman Coding: build an optimal prefix code from symbol frequencies.

A min-heap merges the two lightest trees until one root remains, which is
O(n log n) time and O(n) space for n symbols.
"""
import heapq
import random
from collections import Counter


class Node:
    """Leaf holds a symbol; internal nodes hold children and a summed weight."""

    __slots__ = ("weight", "symbol", "left", "right")

    def __init__(self, weight, symbol=None, left=None, right=None):
        self.weight = weight
        self.symbol = symbol
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.symbol is not None


def build_tree(frequencies):
    """Merge the lightest two trees until one remains. Returns the root."""
    heap = []
    for serial, (symbol, weight) in enumerate(frequencies.items()):
        heapq.heappush(heap, (weight, serial, Node(weight, symbol)))
    if not heap:
        return None
    serial = len(heap)
    while len(heap) > 1:
        weight_a, _, left = heapq.heappop(heap)
        weight_b, _, right = heapq.heappop(heap)
        heapq.heappush(heap, (weight_a + weight_b, serial,
                              Node(weight_a + weight_b, None, left, right)))
        serial += 1
    return heap[0][2]


def build_codes(root):
    """Walk the tree and return {symbol: bit string}."""
    codes = {}
    stack = [(root, "")]
    while stack:
        node, prefix = stack.pop()
        if node.is_leaf():
            codes[node.symbol] = prefix or "0"
        else:
            stack.append((node.left, prefix + "0"))
            stack.append((node.right, prefix + "1"))
    return codes


def encode(text, codes):
    """Replace every character with its code."""
    return "".join(codes[character] for character in text)


def decode(bits, root):
    """Walk the tree for every bit and emit a symbol at each leaf."""
    if root.is_leaf():
        return root.symbol * len(bits)
    output = []
    node = root
    for bit in bits:
        node = node.left if bit == "0" else node.right
        if node.is_leaf():
            output.append(node.symbol)
            node = root
    return "".join(output)


def weighted_path_length(codes, frequencies):
    """Total encoded bits, the quantity Huffman minimises."""
    return sum(len(codes[symbol]) * weight
               for symbol, weight in frequencies.items())


def make_frequencies(n, seed=13):
    """Random frequencies in 1..1000 for n synthetic symbols."""
    rng = random.Random(seed)
    return {f"s{i:05d}": rng.randint(1, 1000) for i in range(n)}


if __name__ == "__main__":
    text = "smart city traffic management"
    frequencies = Counter(text)
    root = build_tree(frequencies)
    codes = build_codes(root)
    encoded = encode(text, codes)
    rebuilt = decode(encoded, root)
    print(f"symbols={len(codes)} chars={len(text)} bits={len(encoded)}")
    for symbol in sorted(codes):
        print(f"{symbol!r:5s} freq={frequencies[symbol]:2d} code={codes[symbol]}")
    print(f"weighted path length={weighted_path_length(codes, frequencies)}")
    print(f"round trip ok={rebuilt == text}")
