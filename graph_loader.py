from igraph import *

ignore_vertices = {46, 19, 9, 18, 27}  # vertices that are not in the biggest connectivity component


def load_graph() -> Graph:
    nodes = get_nodes_map()

    file = open("Edges.csv")
    file.readline()  # skip

    graph = Graph()
    for i, node in nodes.items():
        if i not in ignore_vertices:
            graph.add_vertex(node)
    for line in file:
        u, v, _, edge_id = line.split(',')
        if int(u) not in ignore_vertices:
            graph.add_edge(nodes.get(int(u)), nodes.get(int(v)))

    file.close()
    return graph


def load_graph_with_weights() -> Graph:
    file = open('EdgesWithDistance.txt')
    vertices = set()
    for line in file:
        u, v, _ = line.split()
        vertices.add(u)
        vertices.add(v)
    file.close()

    graph = Graph()
    for vertex in vertices:
        graph.add_vertex(vertex)
    file = open('EdgesWithDistance.txt')

    for line in file:
        u, v, distance = line.split()
        graph.add_edge(u, v, value=int(distance))

    file.close()
    return graph


def get_nodes_map() -> dict[int, str]:
    nodes = dict()
    file = open("Nodes.csv")
    file.readline()  # skip

    for i, line in enumerate(file):
        nodes[i + 1] = line.split(',')[1]

    file.close()
    return nodes
