from graph_loader import load_graph

graph = load_graph()

maximum_clique = graph.largest_cliques()[0]
print(len(maximum_clique))
print(', '.join(graph.vs[i]["name"] for i in maximum_clique))
