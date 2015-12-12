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

def scc_dfs(graph, start, visited, label):
    visited[start] = 0
    parent = []
    children = []
    nodeStack = [start]
    minions = []
    while nodeStack:
        node = nodeStack.pop()
        anteStackLen = len(nodeStack)
        try:
            adjNodes = graph[node]
        except KeyError:
            adjNodes = []
        parent.append(node)
        children.append(adjNodes)
        for w in adjNodes:
            if w not in visited:
                visited[w] = 0
                nodeStack.append(w)
        # determine if current popped node is fully explored
        if len(nodeStack) == anteStackLen:
            visited[node] = label
            minions.append(node)
            label += 1
            children.pop()
            parent.pop()
            # are all the current siblings fully explored
            while children:
                siblings = children.pop()
                allExplored = True
                for sib in siblings:
                    if sib in nodeStack:
                        allExplored = False
                        break
                if not allExplored:
                    children.append(siblings)
                    break
                tail = parent.pop()
                visited[tail] = label
                minions.append(tail)
                label += 1
    return visited, label, minions



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

def scc_loop(graph, qtyNodes):
    visited = {}
    leaders = {}
    label = 1
    for i in range(qtyNodes, 0, -1):
        if i not in visited:
            visited, label, minions = scc_dfs(graph, i, visited, label)
            leaders[i] = minions
    return visited, leaders


def scc_main(file):
    qtyNodes = int(input("how many nodes? "))
    startTime = time.time()
    graphRev = reverse_arcs(file)
    print("--- reverse_arcs() took %s seconds ---" % (time.time() - startTime))
    
    # call scc_loop(graphRev)
    startTime = time.time()
    nodesLabelled, leadersList = scc_loop(graphRev, qtyNodes)
    print("--- 1st pass took %s seconds ---" % (time.time() - startTime))
    leadersList = None    # save memory

    # update graph using nodes' labels
    startTime = time.time()
    newGraph = node_to_label(graphRev, nodesLabelled)
    print("--- node_to_label() took %s seconds ---" % (time.time() - startTime))
    """graphRev popitem()-ed in sub-routine, and is now zero in main as well"""
    nodesLabelled = None
    
    # call scc_loop(graph) with labels changed
    startTime = time.time()
    nodesLabelled, leaders = scc_loop(newGraph, qtyNodes)
    print("--- 2nd pass took %s seconds ---" % (time.time() - startTime))
    nodesLabelled = None
    
    # dfs on newGraph, start w/ leader, only nodes in its scc would be discovered
    startTime = time.time()
    bigFive = [0, 0, 0, 0, 0]
    while leaders:
        sccSize = len(leaders.popitem()[1])
        if sccSize > bigFive[-1]:
            bigFive.pop()
            bigFive.append(sccSize)
            bigFive.sort(reverse=True)
    print("--- comparing scc sizes took %s seconds ---" % (time.time() - startTime))
    print("answer is:", bigFive)
    return bigFive

