from graph_loader import load_graph

graph = load_graph()
largest_stable_set = graph.largest_independent_vertex_sets()[0]

minimum_vertex_covering = list()
for vertex in graph.vs:
    if vertex.index not in largest_stable_set:
        minimum_vertex_covering.append(vertex["name"])

print(len(minimum_vertex_covering))
print(', '.join(minimum_vertex_covering))
