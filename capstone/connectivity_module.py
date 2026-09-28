"""Connectivity module: BFS + DFS traversal order and reachable set."""
from collections import deque


def bfs(network, start):
    """Breadth-first order from start. Returns (order, reachable)."""
    order, seen = [], {start}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in sorted(network.adj[u]):
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return order, seen


def dfs(network, start):
    """Depth-first order from start (iterative). Returns (order, reachable)."""
    order, seen, stack = [], set(), [start]
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        order.append(u)
        for v in sorted(network.adj[u], reverse=True):
            if v not in seen:
                stack.append(v)
    return order, seen


if __name__ == "__main__":
    from route_planner import build_sample_city
    city, _ = build_sample_city()
    b_order, b_reach = bfs(city, "Library")
    d_order, d_reach = dfs(city, "Library")
    print("BFS from Library:", " -> ".join(b_order))
    print("DFS from Library:", " -> ".join(d_order))
    print(f"REACHABLE: {len(b_reach)}/{len(city.nodes())} intersections")
