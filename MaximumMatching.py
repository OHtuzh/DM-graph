from graph_loader import load_graph

graph = load_graph()

largest_matching = list()

while len(graph.es) != 0:
    minimum_degree_sum = 10000000
    min_edge = -1
    for edge in graph.es:
        if graph.vs[edge.source].degree() + graph.vs[edge.target].degree() < minimum_degree_sum:
            minimum_degree_sum = graph.vs[edge.source].degree() + graph.vs[edge.target].degree()
            min_edge = edge
    if min_edge != -1:
        largest_matching.append(graph.vs[min_edge.source]["name"] + " -- " + graph.vs[min_edge.target]["name"])
        graph.delete_vertices([min_edge.source, min_edge.target])


print(len(largest_matching))
print(', '.join(largest_matching))
