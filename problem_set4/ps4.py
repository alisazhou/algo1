
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



def scc_dfs(graph, start, visited, currLabel, minions):
    visited[start] = 0
    heads = graph.get(start)
    if heads:
        for head in heads:
            if head not in visited:
                minions.append(head)
                visited, currLabel, minions = scc_dfs(graph, head, visited, currLabel, minions)
    visited[start] = currLabel
    currLabel += 1
    return visited, currLabel, minions


def scc_loop(graph, qtyNodes):
    visited = {}
    label = 1
    leadersList = {}
    for i in range(qtyNodes, 0, -1):
        if i in graph and i not in visited:
            minions = []
            visited, label, minions = scc_dfs(graph, i, visited, label, minions)
            leadersList[i] = minions
    return visited, leadersList


def node_to_label(oldGraph, labels):
    newGraph = {}
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


def scc_main(file):
    # reverse graph
    qtyNodes = int(input("how many nodes? "))
    graphRev = reverse_arcs(file)
    
    # call scc_loop(graphRev)
    nodesLabelled, leadersList = scc_loop(graphRev, qtyNodes)
    leadersList = None    # save memory
    # update graph using nodes' labels
    newGraph = node_to_label(graphRev, nodesLabelled)
    """graphRev popitem()-ed in sub-routine, and is now zero in main as well"""
    nodesLabelled = None
    
    # call scc_loop(graph) with labels changed
    nodesLabelled, leaders = scc_loop(newGraph, qtyNodes)
    nodesLabelled = None
    
    # dfs on newGraph, start w/ leader, only nodes in its scc would be discovered
    bigFive = [0, 0, 0, 0, 0]
    leadersList = []
    while leaders:
        leadersList.append(leaders.popitem()[0])
    leadersList.sort()
    visited = {}
    while leadersList:
        start = leadersList.pop()
        visited, disregard, scc = scc_dfs(newGraph, start, visited, 0, [])
        size = len(scc) + 1    # plus the leader itself
        if size > bigFive[-1]:
            bigFive.pop()
            bigFive.append(size)
            bigFive.sort(reverse=True)
    return bigFive



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