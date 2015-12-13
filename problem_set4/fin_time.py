"""Second attempt to implement DFS iteratively to find finishing times."""
from copy import deepcopy
import time

def reverse_arcs(file):
    arcs = {}
    with open(file) as f:
        for s in f:
            head, tail = (int(x) for x in s.split(' ')[:2])
            if tail in arcs:
                arcs[tail].append(head)
            else:
                arcs[tail] = [head]
    return arcs
    
def node_to_label(oldGraph, finTimes):
    newGraph = {}
    labels = {}
    for node in finTimes:
        labels[node] = finTimes.index(node) + 1
    while oldGraph:
        head, adjTails = oldGraph.popitem()
        newTail = labels[head]
        for head in adjTails:
            newHead = labels[head]
            if newHead in newGraph:
                newGraph[newHead].append(newTail)
            else:
                newGraph[newHead] = [newTail]
    return newGraph



def dfs(graph, start, explored, finished):
    """Runs DFS from start vertex. Returns explored and finished nodes.
    
    Initialize a stack with start as its element.  Initialize a dict, 
    each node explored is key, its parents is value.
    For each popped node v from the stack, push all of its previously
    unexplored adjacent nodes onto the stack.  v is the parent of these
    nodes. If all of v's have been explored, or if it is a sink vertex,
    mark v as finished.  The index of each node in the finished list is
    its finishing time.
    Returns a dict with node as key and finishing time as value.
    """
    nodeStack = [start]
    children = []
    parents = []
    while nodeStack:
        v = nodeStack.pop()
        explored.append(v)
        try:
            adjs = graph.pop(v)
        except KeyError:
            adjs = []
        # determine if all of v's child nodes have been explored previously
        allExplored = True
        for w in adjs:
            if w not in explored:
                if w not in nodeStack:
                    nodeStack.append(w)
                allExplored = False
        if not allExplored:
            # if not all of v's descendants have been explored, add to lineage
            parents.append(v)
            children.append(adjs)
        else:
            # if all adjacent nodes explored, push v to finished stack
            finished.append(v)
            while children:
                # determine if the parent node is also finished
                siblings = children.pop()
                allExplored2 = True
                for sib in siblings:
                    if sib not in explored:
                        allExplored2 = False
                        break
                if not allExplored2:
                    # return siblings to children, continue popping nodeStack
                    children.append(siblings)
                    break
                else:
                    parent = parents.pop()
                    finished.append(parent)         
    return explored, finished
    
def dfs_loop(graph, qtyNodes):
    """Calls DFS on each unexplored node in descending order.
    
    Args - graph (directed) is represented as an adjacency list, with
    vertices numbered.  Each key is tail, value is list of adjacent
    nodes.
    Initialize two empty lists, one for explored nodes and the other
    for finished nodes.  The index of each node in the finished list is
    its finishing time.
    """
    explored = []
    finished = []
    leaders = {}
    anteFinLen = 0
    for i in range(qtyNodes, 0, -1):
        if i not in explored:
            explored, finished = dfs(graph, i, explored, finished)
            newLen = len(finished)
            sizeScc = newLen - anteFinLen
            anteFinLen = newLen
            leaders[i] = sizeScc
    return finished, leaders

def kosaraju(file):
    """
    """
    qtyNodes = int(input("how many nodes?"))
    
    start_time = time.time()
    graphRev = reverse_arcs(file)
    print("-- reverse took %s seconds ---" % (time.time() - start_time))
    
    start_time = time.time()
    finished, leaders = dfs_loop(deepcopy(graphRev), qtyNodes)
    print("--- pass 1 took %s seconds ---" % (time.time() - start_time))
    
    # graphRev popped in dfs
    start_time = time.time()
    newGraph = node_to_label(graphRev, finished)
    print("--- labelling took %s seconds ---" % (time.time() - start_time))

    start_time = time.time()    
    finished2, leaders2 = dfs_loop(newGraph, qtyNodes)
    print("--- pass 2 took %s seconds ---" % (time.time() - start_time))
    return leaders2
    


"""testcase3_63210:

1   3===6---8
| /   /   /
2---5---7---9   11
  \ | /   \ | / |
    4       10--12
3=6 should be an scc by itself.  instead the algo is discovering them as part
of the 2-5-4 scc
"""