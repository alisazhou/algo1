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
    minions = []
    nodeStack = [start]
    while nodeStack:
        print("pre-pop stack is", nodeStack)
        node = nodeStack.pop()
        print("post-pop stack is", nodeStack)
        try:
            adjNodes = graph.pop(node)
        except KeyError:
            # node is a sink vertex
            visited[node] = label
            print("sink vertex", node, "'s label is", label)
            label += 1
            continue
        for i in adjNodes:
            if i not in visited:
                visited[i] = 0
                minions.append(i)
                nodeStack.append(i)
    minions.reverse()
    print(minions)
    for nion in minions:
        visited[nion] = label
        label += 1
    visited[start] = label
    label += 1
    print("visited for leader", start, "is", visited)
    return visited, minions, label

            
    

def scc_loop(graph, qtyNodes):
    visited = {}
    leadersList = {}
    label = 1
    for i in range(qtyNodes, 0, -1):
        if i not in visited:
            print("leader is now", i)
            visited, minions, label = scc_dfs(graph, i, visited, label)
            leadersList[i] = minions
    return visited

