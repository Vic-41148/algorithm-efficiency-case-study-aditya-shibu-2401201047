"""Connectivity module: BFS + DFS order, reachable set and tree edges."""
from collections import deque


def bfs(network, start):
    """Breadth-first order from start. Returns (order, reachable, tree)."""
    order, seen, tree = [], {start}, []
    queue = deque([start])
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in sorted(network.adj[u]):
            if v not in seen:
                seen.add(v)
                tree.append((u, v))
                queue.append(v)
    return order, seen, tree


def dfs(network, start):
    """Depth-first order from start (iterative). Returns (order, reachable, tree)."""
    order, seen, tree = [], set(), []
    stack = [(start, None)]
    while stack:
        u, parent = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        order.append(u)
        if parent is not None:
            tree.append((parent, u))
        for v in sorted(network.adj[u], reverse=True):
            if v not in seen:
                stack.append((v, u))
    return order, seen, tree


if __name__ == "__main__":
    from route_planner import build_sample_city
    city, _ = build_sample_city()
    b_order, b_reach, b_tree = bfs(city, "Library")
    d_order, d_reach, d_tree = dfs(city, "Library")
    print("BFS from Library:", " -> ".join(b_order))
    print("BFS tree edges:", b_tree)
    print("DFS from Library:", " -> ".join(d_order))
    print("DFS tree edges:", d_tree)
    print(f"REACHABLE: {len(b_reach)}/{len(city.nodes())} intersections")
