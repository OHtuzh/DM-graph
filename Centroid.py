def dfs(gr, current, prev):
    result = 1
    for to in gr[current]:
        if to == prev or to == current:
            continue
        result += dfs(gr, to, current)
    return result


def weight(gr, current, prev='') -> int:
    result = 1
    for to in gr[current]:
        if to == prev:
            continue
        result = max(result, dfs(gr, to, current))
    return result


graph = dict()

file = open('spanning_tree_data.txt')

for line in file:
    data = line.split()
    graph[data[0]] = data[1:]

file.close()


n = len(graph)
min_depth = 1e9
centroid = list()
for node in graph:
    tmp = weight(graph, node)
    if tmp < min_depth:
        min_depth = tmp
        centroid = [node]
    elif tmp == min_depth:
        centroid.append(node)

print(*centroid)
