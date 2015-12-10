import random, copy
import time


def process_adjList(file):
    nums = open(file)
    strList = nums.readlines()        # vertex and its adjacent vertices separated by '\t' in one string
    nums.close()
    adjList = {}
    for vStr in strList:
        vList = []        # vertex and its adjacent vertices as ints in a list
        for s in vStr.strip('\t\n').split('\t'):
            vList.append(int(s))
        adjList[vList[0]] = vList[1:]
    return adjList



def select_edge(adjList):
    v1, v2 = random.sample(adjList.keys(), 2)
    if v2 not in adjList[v1]:
        return select_edge(adjList)
    return (v1, v2)



def contraction(graph):
    """graph represented as an adjacency list:
    adjList = {v1: [adjacent vertices], v2: [adjacent vertices], ... }
    """
    if len(graph) <= 2:
        cut = next(iter(graph.values()))
        return len(cut)
    else:        
#        print(graph)
        v1, v2 = select_edge(graph)
#        print(v2, "contracts into ", v1)
        graph[v1] += graph.pop(v2)
        for adjVers in graph.values():
            while adjVers.count(v2) > 0:
                adjVers.remove(v2)
                adjVers.append(v1)
        while graph[v1].count(v1) > 0:
            graph[v1].remove(v1)
#        print("after contraction: ", graph)
        return contraction(graph)


def repeated_trials(graph):
    n = len(graph)
    minCut = n * (n - 1) / 2    # max number of edges in a graph
    for i in range(100):
        trialGraph = copy.deepcopy(graph)
        cut = contraction(trialGraph)
        if minCut > cut:
            minCut = cut
    return minCut
        
# need to incorporate multiprocessing code


"""test case1:
{1: [2, 3, 4, 7],
 2: [1, 3, 4],
 3: [1, 2, 4],
 4: [1, 2, 3, 5],
 5: [4, 6, 7, 8],
 6: [5, 7, 8],
 7: [1, 5, 6, 8],
 8: [5, 6, 7]}
///expected result: 2
///cuts = (1, 7), (4, 5)

1 4 2 7 3
2 4 1 3
3 1 2 4
4 5 1 2 3
5 8 7 6 4
6 8 5 7
7 6 8 5 1
8 7 6 5
///expected result: 2
///cuts = (1, 7), (4, 5)

{1: [2, 3, 4],
 2: [1, 3, 4],
 3: [1, 2, 4],
 4: [1, 2, 3, 5],
 5: [4, 6, 7, 8],
 6: [5, 7, 8],
 7: [5, 6, 8],
 8: [5, 6, 7]}
///expected result: 1
///cuts = (4, 5)
"""
        