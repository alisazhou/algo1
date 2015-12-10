
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




def scc_dfs(graph, start, visited, currLabel):
    visited[start] = 0
    heads = graph.get(start)
    if heads:
        for head in heads:
            if head not in visited:
                visited, currLabel = scc_dfs(graph, head, visited, currLabel)
    visited[start] = currLabel
    currLabel += 1
    return visited, currLabel


def scc_loop(graph, qtyNodes):
    visited = {}
    label = 1
    for i in range(qtyNodes, 0, -1):
        if i in graph and i not in visited:
            visited, label = scc_dfs(graph, i, visited, label)
    return visited, label


def scc_main(graph):
    # reverse graph
    file = input("file name? ") + ".txt"
    qtyNodes = int(input("how many nodes? "))
    graphRev = parse_file(file, reverse=True)
    SOMETHING = scc_loop(graphRev, qtyNodes)
    
    # call scc_loop(graphRev)
    
    # call scc_loop(graph) with labels changed



"""testcase =
{1: [2, 3],
 2: [4],
 3: [4]}
 
 
{1: [2],
 2: [3],
 3: [5],
 4: [2],
 5: [4, 6]}
 
{1: [2, 3, 4],
 2: [4, 5],
 3: [5],
 5: [4]}
"""