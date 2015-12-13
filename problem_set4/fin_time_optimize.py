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

def dfs(graph, start, explored, label):
    path = []
    nodeStack = [start]
    minions = 0
    while nodeStack:
        v = nodeStack.pop()
        explored[v] = 'discovered'
        # are all of v's adj nodes discovered?
        try:
            adjs = graph[v]
        except KeyError:
            adjs = []
        allDiscovered = True
        for w in adjs:
            if w not in explored:
                explored[w] = 'undiscovered'
                nodeStack.append(w)
                allDiscovered = False
        # if not all discovered, append v to path, continue with popping stack
        if not allDiscovered:
            path.append(v)
        # if all discovered, assign label to v, ie mark it as finished
        else:
            explored[v] = label
            label += 1
            minions += 1
            while path:
                pred = path.pop()
                siblings = graph[pred]
                # are all of the predecessor's adj nodes discovered?
                allDiscovered2 = True
                for sib in siblings:
                        allDiscovered2 = False
                        break
                # if not all discovered, replace pred in path, continue w/ stack
                if not allDiscovered2:
                    path.append(pred)
                    break
                # if all discovered, assign label to pred, continue w/ path
                else:
                    explored[pred] = label
                    label += 1
                    minions += 1
    return explored, label, minions


def dfs_loop(graph, qtyNodes, pass2=False):
    explored = {}
    label = 1
    bigFive = [0, 0, 0, 0, 0]
    timeStamp = time.time()
    for i in range(qtyNodes, 0, -1):
        if i not in explored:
            explored, label, minions = dfs(graph, i, explored, label)
            if pass2:
                if minions > bigFive[-1]:
                    bigFive.pop()
                    bigFive.append(minions)
                    bigFive.sort(reverse=True)
        if i % 100000 == 0:
            print("--- at node %s, took %s seconds ----"
                  % (i, time.time() - timeStamp)
                 )
    if pass2:
        return bigFive
    else:
        return explored


def scc_main(file, qtyNodes):

    start_time = time.time()
    graphRev = reverse_arcs(file)
    print("---reverse %s seconds---" % (time.time() - start_time))
    
    start_time = time.time()
    label = dfs_loop(graphRev, qtyNodes)
    print("---pass1 %s seconds---" % (time.time() - start_time))
    
    start_time = time.time()
    newGraph = node_to_label(graphRev, label)
    print("---labelling %s seconds---" % (time.time() - start_time))
    
    start_time = time.time()
    bigFive = dfs_loop(newGraph, qtyNodes, pass2=True)
    print("---pass2 %s seconds---" % (time.time() - start_time))
    
    return bigFive