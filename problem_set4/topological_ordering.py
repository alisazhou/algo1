def parse_file(file, reverse=False):
    arcs = {}
    with open(file) as f:
        for s in f:
            tail, head = (int(x) for x in s.split(' ')[:2])
            if reverse:
                tail, head = head, tail
            if tail in arcs:
                arcs[tail].append(head)
            else:
                arcs[tail] = [head]
    return arcs
    

def topo_dfs(graph, start, visited, currLabel):
    visited[start] = 0
    heads = graph.get(start)
    if heads:
        for head in heads:
            if head not in visited:
                visited, currLabel = topo_dfs(graph, head, visited, currLabel)
    visited[start] = currLabel
    currLabel -= 1
    return visited, currLabel


def topo_order(graph):
    visited = {}
    currLabel = int(input("how many nodes: "))
    for tail in graph:
        if tail not in visited:
            visited, currLabel = topo_dfs(graph, tail, visited, currLabel)
    return visited
