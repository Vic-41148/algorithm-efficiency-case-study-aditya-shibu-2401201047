"""Route planning module: road network model + Dijkstra with trace."""
import csv
import heapq


class RoadNetwork:
    """Undirected weighted graph. Nodes = intersections, edges = roads."""

    def __init__(self):
        self.adj = {}   # node -> {neighbor: weight}

    def add_intersection(self, name):
        self.adj.setdefault(name, {})

    def add_road(self, u, v, w, two_way=True):
        self.add_intersection(u)
        self.add_intersection(v)
        self.adj[u][v] = w
        if two_way:
            self.adj[v][u] = w

    def nodes(self):
        return sorted(self.adj)

    def roads(self):
        seen, out = set(), []
        for u, nbrs in self.adj.items():
            for v, w in nbrs.items():
                if (v, u) not in seen:
                    seen.add((u, v))
                    out.append((u, v, w))
        return sorted(out)

    def adjacency_list(self):
        return {u: sorted(nbrs.items()) for u, nbrs in sorted(self.adj.items())}

    def adjacency_matrix(self):
        nodes = self.nodes()
        idx = {n: i for i, n in enumerate(nodes)}
        n = len(nodes)
        mat = [[0] * n for _ in range(n)]
        for u, v, w in self.roads():
            mat[idx[u]][idx[v]] = w
            mat[idx[v]][idx[u]] = w
        return nodes, mat


def load_network(source):
    """Build a network from CSV rows with from, to and weight columns.

    source may be a path or an open text file, such as io.StringIO.
    """
    if hasattr(source, "read"):
        return _load_rows(source)
    with open(source, newline="") as handle:
        return _load_rows(handle)


def _load_rows(handle):
    network = RoadNetwork()
    for row in csv.DictReader(handle):
        network.add_road(row["from"].strip(), row["to"].strip(),
                         int(row["weight"]))
    return network


def dijkstra(network, source, dest):
    """Shortest path. Returns (path, cost, trace) where trace lists
    each settled node with its final distance, in settle order."""
    dist = {n: float("inf") for n in network.nodes()}
    prev = {}
    dist[source] = 0
    pq, visited, trace = [(0, source)], set(), []
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        trace.append((u, d))
        if u == dest:
            break
        for v, w in network.adj[u].items():
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
    if dist[dest] == float("inf"):
        return [], float("inf"), trace
    path, cur = [], dest
    while cur != source:
        path.append(cur)
        cur = prev[cur]
    path.append(source)
    return path[::-1], dist[dest], trace


def build_sample_city():
    """Deterministic 10-intersection demo city with fixed coordinates."""
    city = RoadNetwork()
    roads = [
        ("Library", "Station", 4), ("Library", "Park", 3),
        ("Station", "Hospital", 5), ("Station", "Market", 6),
        ("Park", "Market", 2), ("Park", "Museum", 7),
        ("Hospital", "University", 3), ("Hospital", "Mall", 8),
        ("Market", "Mall", 4), ("Market", "Stadium", 5),
        ("Museum", "Stadium", 3), ("University", "Airport", 6),
        ("Mall", "Airport", 4), ("Stadium", "Airport", 7),
    ]
    for u, v, w in roads:
        city.add_road(u, v, w)
    coords = {
        "Library": (0, 4), "Station": (2, 5), "Park": (1, 2),
        "Hospital": (4, 6), "Market": (3, 3), "Museum": (2, 0),
        "University": (6, 7), "Mall": (5, 4), "Stadium": (4, 1),
        "Airport": (7, 3),
    }
    return city, coords


if __name__ == "__main__":
    city, _ = build_sample_city()
    csv_city = load_network("sample_roads.csv")
    print("CSV LOAD: sample_roads.csv ->",
          len(csv_city.nodes()), "intersections,",
          len(csv_city.roads()), "roads")
    print("NODES:", city.nodes())
    print("ROADS:", len(city.roads()))
    print("ADJACENCY LIST:")
    for u, nbrs in city.adjacency_list().items():
        print(f"  {u}: {nbrs}")
    nodes, matrix = city.adjacency_matrix()
    print("ADJACENCY MATRIX (0 = no road):")
    print(f"{'':>11}" + "".join(f"{n[:4]:>5}" for n in nodes))
    for n, row in zip(nodes, matrix):
        print(f"{n:>11}" + "".join(f"{x:>5}" for x in row))
    print(f"MATRIX: {len(nodes)} x {len(nodes)} = {len(nodes) ** 2} cells; "
          f"list holds {2 * len(city.roads())} directed entries")
    path, cost, trace = dijkstra(city, "Library", "Airport")
    print(f"DIJKSTRA Library -> Airport: {' -> '.join(path)} cost={cost}")
    print("TRACE (settled node, distance):")
    for u, d in trace:
        print(f"  {u}: {d}")
