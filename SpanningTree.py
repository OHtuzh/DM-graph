from graph_loader import load_graph_with_weights

graph = load_graph_with_weights()

spanning_tree = graph.spanning_tree()
for vertex in spanning_tree.vs:
    targets = list()
    for edge in spanning_tree.es:
        if spanning_tree.vs[edge.source] == vertex or spanning_tree.vs[edge.target] == vertex:
            targets.append(spanning_tree.vs[edge.target]["name"])
    print(f"{vertex['name']}:", ', '.join(targets))

