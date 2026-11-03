"""Write the congestion scenario table used in the report."""
import csv

from route_planner import build_sample_city
from traffic_analysis import compare_routes

SCENARIOS = [
    ("Library -> Airport", "Market-Mall + Mall-Airport",
     [("Market", "Mall"), ("Mall", "Airport")], 3),
    ("Library -> Airport", "Library-Park", [("Library", "Park")], 3),
    ("Library -> Airport", "Park-Market", [("Park", "Market")], 3),
    ("Library -> Airport", "Park-Museum", [("Park", "Museum")], 3),
]

city, _ = build_sample_city()
rows = []
for trip, label, jam, factor in SCENARIOS:
    r = compare_routes(city, "Library", "Airport", jam, factor)
    rows.append({
        "trip": trip,
        "jammed_roads": label,
        "factor": factor,
        "original_route": " -> ".join(r["original"][0]),
        "original_cost": r["original"][1],
        "congested_route": " -> ".join(r["congested"][0]),
        "congested_cost": r["congested"][1],
        "delta": r["delta"],
        "rerouted": "yes" if r["rerouted"] else "no",
    })

with open("data/congestion_scenarios.csv", "w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

for row in rows:
    print(f"{row['jammed_roads']:32} x{row['factor']}  "
          f"{row['original_cost']:>3} -> {row['congested_cost']:>3}  "
          f"delta {row['delta']:>2}  rerouted {row['rerouted']}")
print("saved data/congestion_scenarios.csv")
