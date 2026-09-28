"""Traffic analysis module: Bellman-Ford + congestion simulation."""
from route_planner import dijkstra


def bellman_ford(network, source):
    """Shortest paths from source. Returns (dist, prev, trace, ok) where
    trace records every relaxation round and ok=False on negative cycle."""
    nodes = network.nodes()
    dist = {n: float("inf") for n in nodes}
    prev = {}
    dist[source] = 0
    trace = []
    for i in range(len(nodes) - 1):
        changed = 0
        for u, v, w in network.roads():
            for a, b in ((u, v), (v, u)):
                if dist[a] + w < dist[b]:
                    dist[b] = dist[a] + w
                    prev[b] = a
                    changed += 1
        trace.append((i + 1, changed))
        if changed == 0:
            break
    ok = True
    for u, v, w in network.roads():
        for a, b in ((u, v), (v, u)):
            if dist[a] + w < dist[b]:
                ok = False
    return dist, prev, trace, ok


def path_from_prev(prev, source, dest):
    if dest == source:
        return [source]
    if dest not in prev:
        return []
    path, cur = [], dest
    while cur != source:
        path.append(cur)
        cur = prev[cur]
    path.append(source)
    return path[::-1]


def apply_congestion(network, congested_edges, factor):
    """Copy of network with listed roads scaled by factor. Returns new network."""
    from route_planner import RoadNetwork
    busy = RoadNetwork()
    congested = {tuple(sorted(e)) for e in congested_edges}
    for u, v, w in network.roads():
        busy.add_road(u, v, w * factor if tuple(sorted((u, v))) in congested else w)
    return busy


def compare_routes(network, source, dest, congested_edges, factor):
    """Original vs congested shortest routes. Returns dict with both."""
    p0, c0, _ = dijkstra(network, source, dest)
    busy = apply_congestion(network, congested_edges, factor)
    p1, c1, _ = dijkstra(busy, source, dest)
    return {"original": (p0, c0), "congested": (p1, c1),
            "delta": c1 - c0, "rerouted": p0 != p1}


if __name__ == "__main__":
    from route_planner import build_sample_city
    city, _ = build_sample_city()
    dist, prev, trace, ok = bellman_ford(city, "Library")
    print("BELLMAN-FORD from Library (distances):")
    for n in city.nodes():
        print(f"  {n}: {dist[n]}")
    print("ROUNDS (round, relaxations):", trace, "no-negative-cycle:", ok)
    jam = [("Market", "Mall"), ("Mall", "Airport")]
    r = compare_routes(city, "Library", "Airport", jam, 3)
    print("ORIGINAL:", " -> ".join(r["original"][0]), "cost=", r["original"][1])
    print("CONGESTED:", " -> ".join(r["congested"][0]), "cost=", r["congested"][1])
    print("DELTA:", r["delta"], "REROUTED:", r["rerouted"])
