"""Streamlit app: traffic management with 4 modules."""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from route_planner import RoadNetwork, dijkstra, build_sample_city
from traffic_analysis import bellman_ford, compare_routes
from connectivity_module import bfs, dfs
from mst_planner import prim, kruskal

st.set_page_config(page_title="Smart City Traffic", layout="wide")
st.title("Smart City Traffic Management and Route Optimization")

if "city" not in st.session_state:
    st.session_state.city, st.session_state.coords = build_sample_city()
city = st.session_state.city

tab_route, tab_traffic, tab_conn, tab_mst = st.tabs(
    ["Route Planning", "Traffic Analysis", "Connectivity", "Infrastructure"])

with tab_route:
    st.header("Route Planning (Dijkstra)")
    nodes = city.nodes()
    src = st.selectbox("Source", nodes, index=nodes.index("Library"))
    dst = st.selectbox("Destination", nodes, index=nodes.index("Airport"))
    if st.button("Find route"):
        path, cost, trace = dijkstra(city, src, dst)
        st.write(f"Route: {' -> '.join(path)}")
        st.write(f"Total cost: {cost}")
        st.write("Settle order:", [u for u, _ in trace])

with tab_traffic:
    st.header("Traffic Analysis (Bellman-Ford + congestion)")
    edges = [f"{u} - {v} ({w})" for u, v, w in city.roads()]
    jam = st.multiselect("Congested roads", edges)
    factor = st.slider("Congestion factor", 2, 5, 3)
    src2 = st.selectbox("Source", nodes, index=nodes.index("Library"), key="t_src")
    dst2 = st.selectbox("Destination", nodes, index=nodes.index("Airport"), key="t_dst")
    if st.button("Compare routes"):
        picked = []
        for item in jam:
            u, v = item.split(" (")[0].split(" - ")
            picked.append((u, v))
        r = compare_routes(city, src2, dst2, picked, factor)
        st.write("Original:", " -> ".join(r["original"][0]), r["original"][1])
        st.write("Congested:", " -> ".join(r["congested"][0]), r["congested"][1])
        st.write(f"Delta: +{r['delta']}, rerouted: {r['rerouted']}")

with tab_conn:
    st.header("Network Connectivity (BFS / DFS)")
    start = st.selectbox("Start intersection", nodes, index=0)
    if st.button("Traverse"):
        b_order, b_reach = bfs(city, start)
        d_order, d_reach = dfs(city, start)
        st.write("BFS:", " -> ".join(b_order))
        st.write("DFS:", " -> ".join(d_order))
        st.write(f"Reachable: {len(b_reach)}/{len(nodes)}")

with tab_mst:
    st.header("Infrastructure Planning (Prim / Kruskal)")
    if st.button("Build MST"):
        pe, pt = prim(city)
        ke, kt = kruskal(city)
        st.table(pd.DataFrame(pe, columns=["From", "To", "Cost"]))
        st.write(f"Prim total: {pt} | Kruskal total: {kt} | agree: {pt == kt}")
