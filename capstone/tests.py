"""Unit tests for the smart city traffic modules."""
import unittest

from route_planner import build_sample_city, load_network, dijkstra
from traffic_analysis import bellman_ford, compare_routes
from connectivity_module import bfs, dfs
from mst_planner import prim, kruskal, UnionFind


class TestTrafficSystem(unittest.TestCase):
    def setUp(self):
        self.city, _ = build_sample_city()

    def test_mst_agreement(self):
        pe, pt = prim(self.city)
        ke, kt = kruskal(self.city)
        self.assertEqual(pt, 33)
        self.assertEqual(pt, kt)
        self.assertEqual(len(pe), len(self.city.nodes()) - 1)

    def test_dijkstra_matches_bellman_ford(self):
        path, cost, _ = dijkstra(self.city, "Library", "Airport")
        dist, _, _, ok = bellman_ford(self.city, "Library")
        self.assertEqual(cost, 13)
        self.assertEqual(cost, dist["Airport"])
        self.assertTrue(ok)
        self.assertEqual(" -> ".join(path),
                         "Library -> Park -> Market -> Mall -> Airport")

    def test_bfs_reaches_all(self):
        order, reach, tree = bfs(self.city, "Library")
        self.assertEqual(len(reach), len(self.city.nodes()))
        self.assertEqual(len(order), 10)
        self.assertEqual(len(tree), 9)

    def test_dfs_tree_edges(self):
        order, reach, tree = dfs(self.city, "Library")
        self.assertEqual(len(reach), len(self.city.nodes()))
        self.assertEqual(len(tree), 9)
        self.assertEqual({child for _, child in tree},
                         set(self.city.nodes()) - {"Library"})

    def test_disconnected_network(self):
        self.city.add_intersection("Island")
        path, cost, _ = dijkstra(self.city, "Library", "Island")
        self.assertEqual(path, [])
        self.assertEqual(cost, float("inf"))
        _, reach, _ = bfs(self.city, "Library")
        self.assertEqual(len(reach), 10)
        self.assertEqual(len(self.city.nodes()), 11)

    def test_union_find_merges(self):
        uf = UnionFind(["a", "b", "c"])
        self.assertTrue(uf.union("a", "b"))
        self.assertFalse(uf.union("a", "b"))
        self.assertEqual(uf.find("a"), uf.find("b"))
        self.assertTrue(uf.union("b", "c"))
        self.assertEqual(uf.find("a"), uf.find("c"))

    def test_congestion_reroutes(self):
        r = compare_routes(self.city, "Library", "Airport",
                           [("Market", "Mall"), ("Mall", "Airport")], 3)
        self.assertTrue(r["rerouted"])
        self.assertEqual(r["original"][1], 13)
        self.assertEqual(r["congested"][1], 17)
        self.assertEqual(r["delta"], 4)

    def test_congestion_off_route(self):
        r = compare_routes(self.city, "Library", "Airport",
                           [("Park", "Museum")], 3)
        self.assertFalse(r["rerouted"])
        self.assertEqual(r["delta"], 0)

    def test_adjacency_matrix(self):
        nodes, matrix = self.city.adjacency_matrix()
        self.assertEqual(len(nodes), 10)
        self.assertEqual(sum(1 for row in matrix for w in row if w), 28)
        for i in range(len(nodes)):
            self.assertEqual(matrix[i][i], 0)
            for j in range(len(nodes)):
                self.assertEqual(matrix[i][j], matrix[j][i])

    def test_csv_loader(self):
        net = load_network("sample_roads.csv")
        self.assertEqual(len(net.nodes()), 10)
        self.assertEqual(len(net.roads()), 14)
        _, cost, _ = dijkstra(net, "Library", "Airport")
        self.assertEqual(cost, 13)


if __name__ == "__main__":
    unittest.main()
