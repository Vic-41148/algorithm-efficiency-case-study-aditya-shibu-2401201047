"""Streamlit app: traffic management with 4 modules."""
import io

import streamlit as st
import pandas as pd

from route_planner import load_network, dijkstra, build_sample_city
from traffic_analysis import bellman_ford, compare_routes
from connectivity_module import bfs, dfs
from mst_planner import prim, kruskal

st.set_page_config(page_title="Smart City Traffic", layout="wide")
st.title("Smart City Traffic Management and Route Optimization")

with st.sidebar:
    st.header("Road network")
    upload = st.file_uploader("Load roads CSV", type=["csv"])
    st.caption("CSV columns: from, to, weight")
    if upload is not None:
        city = load_network(io.StringIO(upload.getvalue().decode("utf-8")))
        st.caption(f"Loaded {len(city.nodes())} intersections, "
                   f"{len(city.roads())} roads")
    else:
        if "city" not in st.session_state:
            st.session_state.city, st.session_state.coords = build_sample_city()
        city = st.session_state.city
        st.caption("Sample city: 10 intersections, 14 roads")


def default_index(nodes, name):
    return nodes.index(name) if name in nodes else 0


tab_route, tab_traffic, tab_conn, tab_mst = st.tabs(
    ["Route Planning", "Traffic Analysis", "Connectivity", "Infrastructure"])

with tab_route:
    st.header("Route Planning (Dijkstra)")
    nodes = city.nodes()
    src = st.selectbox("Source", nodes, index=default_index(nodes, "Library"),
                       key="r_src")
    dst = st.selectbox("Destination", nodes, index=default_index(nodes, "Airport"),
                       key="r_dst")
    if st.button("Find route"):
        path, cost, trace = dijkstra(city, src, dst)
        st.write(f"Route: {' -> '.join(path)}")
        st.write(f"Total cost: {cost}")
        st.write("Settle order:", " -> ".join(u for u, _ in trace))
    with st.expander("Adjacency matrix"):
        labels, matrix = city.adjacency_matrix()
        st.dataframe(pd.DataFrame(matrix, index=labels, columns=labels))

with tab_traffic:
    st.header("Traffic Analysis (Bellman-Ford + congestion)")
    nodes = city.nodes()
    edge_map = {f"{u} - {v} ({w})": (u, v) for u, v, w in city.roads()}
    jam = st.multiselect("Congested roads", list(edge_map))
    factor = st.slider("Congestion factor", 2, 5, 3)
    src2 = st.selectbox("Source", nodes, index=default_index(nodes, "Library"),
                        key="t_src")
    dst2 = st.selectbox("Destination", nodes, index=default_index(nodes, "Airport"),
                        key="t_dst")
    if st.button("Compare routes"):
        picked = [edge_map[item] for item in jam]
        r = compare_routes(city, src2, dst2, picked, factor)
        st.write("Original:", " -> ".join(r["original"][0]), r["original"][1])
        st.write("Congested:", " -> ".join(r["congested"][0]), r["congested"][1])
        st.write(f"Delta: +{r['delta']}, rerouted: {r['rerouted']}")

with tab_conn:
    st.header("Network Connectivity (BFS / DFS)")
    nodes = city.nodes()
    start = st.selectbox("Start intersection", nodes,
                         index=default_index(nodes, "Library"))
    if st.button("Traverse"):
        b_order, b_reach, b_tree = bfs(city, start)
        d_order, d_reach, d_tree = dfs(city, start)
        st.write("BFS:", " -> ".join(b_order))
        st.write("DFS:", " -> ".join(d_order))
        st.write(f"Reachable: {len(b_reach)}/{len(nodes)}")
        st.write(f"Tree edges: BFS {len(b_tree)}, DFS {len(d_tree)}")

with tab_mst:
    st.header("Infrastructure Planning (Prim / Kruskal)")
    if st.button("Build MST"):
        pe, pt = prim(city)
        ke, kt = kruskal(city)
        st.table(pd.DataFrame(pe, columns=["From", "To", "Cost"]))
        st.write(f"Prim total: {pt} | Kruskal total: {kt} | agree: {pt == kt}")
