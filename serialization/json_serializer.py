import json


def export_graph(graph, output_path="output.json"):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(graph.to_dict(), f, indent=2)