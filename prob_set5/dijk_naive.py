def get_graph(file):
    """Process directed graph in txt, return an adjacency list in dict.
    
    Keys are nodes, values are tuples of adjacent edges and lengths.
    The first elem of each tuple is the edge's head, the second elem is
    the edge's length.
    """
    graph = {}
    with open(file) as f:
        for s in f:
            node = s.rstrip().split()
            vertex = int(node[0])
            edges = []
            edgesStr = node[1:]
            for edge in edgesStr:
                _, __ = edge.split(',')
                edgeTup = (int(_), int(__))
                edges.append(edgeTup)
            graph[vertex] = edges
    return graph

def dijkstra_shortest_path(graph):
    """Naive implementation of Dijkstra's Algo, O(mn) time.

    Do exhaustive search for shortest path when adding each node.
    For all crossing edges (those pointing from a processed node to an
    unprocessed node), add to processed the new node with the shortest
    path from source to any crossing edge nodes.  Continue the process
    until all nodes have been processed to get the shortest path to
    each node in the graph.
    """
    processedNodes = [1]
    distances = {1: 0}
    path = {1:[]}
    while len(processedNodes) < len(graph):
        wStar = 0
        # if no path exists to a node, its distance to source is 1000000
        shortestPath = 1000000
        for v in processedNodes:
            for w, vToW in graph[v]:
                if w in processedNodes:
                    # only consider crossing edges
                    continue
                else:
                    # shortest path to frontier node has been calculated
                    sourceToW = distances[v] + vToW
                    if sourceToW <= shortestPath:
                        wStar = w
                        shortestPath = sourceToW
                        path[wStar] = path[v] + [v]
        processedNodes.append(wStar)
        distances[wStar] = shortestPath
    return distances



if __name__ == "__main__":
    graph = get_graph("dijkstraData.txt")
    distances = dijkstra_shortest_path(graph)
    nodesNeeded = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for node in nodesNeeded:
        print(node, distances[node])
    """answer: 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068"""
