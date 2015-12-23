#!/usr/bin/python
"""
File: hmwk4.py
Author: Conrad
Description: implement dfs and compute SCCs
"""

from collections import defaultdict

class Graph(object):

    def __init__(self, edges):
        self.adj_list = defaultdict(list)
        maximum = 0
        for tail, head in edges:
            int_tail = int(tail)
            int_head = int(head)
            if int_tail > maximum:
                maximum = int_tail
            if int_head > maximum:
                maximum = int_head
            self.adj_list[int(tail)].append(int(head))

        # the below doesn't work because not all vertices are tails'
        ## self.checked = dict((key, False) for key in self.adj_list)
        self.checked = dict((counter, False) for counter in xrange(1, maximum + 1))

        # order is just another way to save the "running time"
        # element 0 has running time 1, element 1 has running time 2 etc
        self.order = []
        self.leader = defaultdict(list)

    def dfs(self, start_vertex, get_order=False, source=None):
        """call self.checked etc after dfs() to see results"""
        self.checked[start_vertex] = True

        if source:
            self.leader[source].append(start_vertex)

        for head in self.adj_list[start_vertex]:
            if not self.checked[head]:
                # this chgs self.checked, self.order, self.leader
                self.dfs(head,
                         get_order=get_order,
                         source=source)

        if get_order:
            # get appended if you are a leaf node or you already finished
            # exploring all your child nodes
            self.order.append(start_vertex)

def overview():
    """
    first iteration on reversed graph should keep track of running time
    ie. count down vertices

    second interation on actual graph should keep track of "leader"
    """

    """
    test_case = [(1, 4), (2, 8), (3, 6), (4, 7), (5, 2), (6, 9),
                 (7, 1), (8, 5), (8, 6), (9, 7), (9, 3),]
    data = test_case

    """
    data = []
    with open('SCC.txt', 'rb') as data_file:
    ## with open('test_scc.txt', 'rb') as data_file:
        for line in data_file.readlines():
            line = line.decode('utf8')
            data.append(line.rstrip().split(' '))
            # note this data is still in string format

    reverse_graph = Graph((head, tail) for tail, head in data)
    reverse_graph.dfs(1, get_order=True)

    ## print reverse_graph.checked
    ## print reverse_graph.adj_list

    for vertex in reverse_graph.checked:
        if not reverse_graph.checked[vertex]:
            reverse_graph.dfs(vertex, get_order=True)
    # print reverse_graph.order
    ## print 'done reverse: order is', reverse_graph.order[:5]

    graph = Graph(data)
    while reverse_graph.order:
        source = reverse_graph.order.pop()
        if graph.checked[source]:
            continue
        graph.dfs(source, source=source)

    # make this find the 5 biggest leaders
    if len(graph.leader) > 5:
        for i in range(5):
            # get the biggest scc (with the most vertices)
            vertex = max(graph.leader, key=lambda source: len(graph.leader[source]))
            print(vertex, len(graph.leader[vertex]))
            graph.leader.pop(vertex)
    else:
        for source in graph.leader:
            print('scc with leader {}, {} components: {}'.format(source,
                                                                         len(graph.leader[source]),
                                                                         graph.leader[source]))



if __name__ == '__main__':
    import sys, threading, time
    start_time = time.time()
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=overview)
    thread.start()
    print("---finished in %s seconds---" % (time.time() - start_time))



