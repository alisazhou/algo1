from heapq import heappush, heappop, heapify

def get_graph(file):
    """Process directed graph in txt, return an adjacency list in dict.
    
    Keys are nodes, values are tuples of adjacent edges and lengths.
    The second elem of each tuple is the edge's head, the first elem is
    the edge's length, the third element repeats the node itself.
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
                edgeTup = (int(__), int(_), vertex)
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
    processedNodes = [1]
    distances = {1:0}
    path = {1:[]}
    greedyScoreHeap = graph[1]
    heapify(greedyScoreHeap)
    
    while len(processedNodes) < len(graph):
        # heappop to get the min value of all Dijk scores
        # add popped node to processed nodes
        dijkScore, wStar, vStar = heappop(greedyScoreHeap)
        processedNodes.append(wStar)
        distances[wStar] = dijkScore
        path[wStar] = path[vStar] + [v]
        # delete arcs that no long "cross", ie used to point to wStar
        
        # new crossing edges, ie point from wStar to unprocessed nodes
        # calculate new Dijk score for each now with wStar in processed
        # if node not in heap, add its Dijk score to heap
        # if node already in heap, update its Dijk score if necessary
        
    # for each unprocessed node, find their greedy Dijkstra score
    # insert node into heap, using Dijk score as key
    # then for all crossing edges, choose node with min Dijk score
