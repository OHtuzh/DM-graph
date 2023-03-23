from graph_loader import load_graph_with_weights
from igraph import *

graph = Graph()

spanning_tree = load_graph_with_weights().spanning_tree()
cycles_edges = list()
for edge in spanning_tree.es:
    if edge.source == edge.target:
        cycles_edges.append(edge.index)

spanning_tree.delete_vertices(cycles_edges)
print(', '.join(f"{spanning_tree.vs[i]['name']} -- {i}" for i in spanning_tree.to_prufer()))
