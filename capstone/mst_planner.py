"""Infrastructure module: Prim + Kruskal minimum spanning trees."""


class UnionFind:
    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}
        self.rank = {n: 0 for n in nodes}

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


def prim(network, start=None):
    """Grow MST from cheapest frontier edge. Returns (edges, total)."""
    import heapq
    nodes = network.nodes()
    start = start or nodes[0]
    visited, edges, total = {start}, [], 0
    pq = [(w, start, v) for v, w in network.adj[start].items()]
    heapq.heapify(pq)
    while pq and len(visited) < len(nodes):
        w, u, v = heapq.heappop(pq)
        if v in visited:
            continue
        visited.add(v)
        edges.append((u, v, w))
        total += w
        for to, w2 in network.adj[v].items():
            if to not in visited:
                heapq.heappush(pq, (w2, v, to))
    return sorted(edges), total


def kruskal(network):
    """Sort all roads, take cheapest that connects components."""
    uf = UnionFind(network.nodes())
    edges, total = [], 0
    for u, v, w in sorted(network.roads(), key=lambda e: e[2]):
        if uf.union(u, v):
            edges.append((u, v, w))
            total += w
    return sorted(edges), total


if __name__ == "__main__":
    from route_planner import build_sample_city
    city, _ = build_sample_city()
    pe, pt = prim(city)
    ke, kt = kruskal(city)
    print("PRIM MST:") 
    for e in pe:
        print(f"  {e[0]} - {e[1]} ({e[2]})")
    print("PRIM TOTAL:", pt)
    print("KRUSKAL TOTAL:", kt, "SAME:", pt == kt)
