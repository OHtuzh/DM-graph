from graph_loader import load_graph

graph = load_graph()

maximum_stable_set = graph.largest_independent_vertex_sets()[0]
print(len(maximum_stable_set))
print(', '.join(graph.vs[i]["name"] for i in maximum_stable_set))

