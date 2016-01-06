from heapq import heappush, heappop, heapify

def get_graph(file):
    """Process directed graph in txt, return an adjacency list in dict.
    
    Keys are nodes, values are tuples of adjacent edges and lengths.
    The second elem of each tuple is the edge's head, the first elem is
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
                edgeTup = (int(__), int(_))
                edges.append(edgeTup)
            graph[vertex] = edges
    return graph


def dijkstra_shortest_path(graph):
    """Heap implementation of Dijkstra's algorithm.

    Elements in heap represent unprocessed nodes. Key of an elem is the
    smallest Dijkstra greedy score of any crossing edge pointing to this
    node. By invariant, the extract_min yields the correct vertex wStar
    to add to processed next, and then set A[wStar] to key[wStar].
    """
    distances = {1:0}
    path = {1:[]}
    greedyScoreHeap = []
    for edgeLen, tail in graph[1]:
        heappush(greedyScoreHeap, (edgeLen, tail, 1))
    removedFromHeap = []

    while len(distances) < len(graph):
        # heappop to get the min value of all Dijk scores
        while True:
            sourceToWstar, wstar, vstar = heappop(greedyScoreHeap)
            if wstar not in removedFromHeap:
                break
        # add popped node to processed nodes
        distances[wstar] = sourceToWstar
        path[wstar] = path[vstar] + [vstar]
        # delete arcs that no longer "cross", ie used to point to wStar
        removedFromHeap.append(wstar)
        # new crossing edges, ie point from wStar to unprocessed nodes
        for edgeLen, node in graph[wstar]:
            # only if node has not been processed
            if node not in distances:
                sourceToNode = sourceToWstar + edgeLen
                heappush(greedyScoreHeap, (sourceToNode, node, wstar))

    return distances



if __name__ == "__main__":
    import time
    startTime = time.time()
    graph = get_graph("dijkstraData.txt")
    distances = dijkstra_shortest_path(graph)
    nodesNeeded = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for node in nodesNeeded:
        print(node, distances[node])
    print("---- %s seconds ----" % (time.time() - startTime))
    """answer: 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068"""
