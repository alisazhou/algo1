from itertools import combinations

def find_closest(sortedPoints):
    if len(sortedPoints) <= 3:
        return all_pairwise_dist(sortedPoints)
    else:
        mid = len(sortedPoints) // 2
        smallestLeft, closestLeft = find_closest(sortedPoints[:mid])
        smallestRight, closestRight = find_closest(sortedPoints[mid:])
        if smallestLeft <= smallestRight:
            delta = smallestLeft
            candidates = {delta: closestLeft}
        else:
            delta = smallestRight
            candidates = {delta: closestRight}
        xBar = sortedPoints[mid][0]
        splitClose = []
        for point in sortedPoints:
            if point[0] >= xBar - delta and point[0] <= xBar + delta:
                splitClose.append(point)
        splitsByY = sorted(splitClose, key=lambda point: point[1])
        smallestSplit, closestSplit = closest_split_pair(splitsByY)
        if smallestSplit < delta:
            delta = smallestSplit
            candidates[delta] = closestSplit
        return delta, candidates[delta]

def closest_split_pair(splits):
    candidates = {}
    for i in range(len(splits) - 1):
        j = min(i+8, len(splits))
        nextSeven = splits[i:j]
        closest, pair = all_pairwise_dist(nextSeven)
        candidates[closest] = pair
    smallestDist = min(candidates.keys())
    return smallestDist, candidates[smallestDist]
        


def euc_dist(pointA, pointB):
    xa, ya = pointA[0], pointA[1]
    xb, yb = pointB[0], pointB[1]
    return ((xa - xb)**2 + (ya - yb)**2)**0.5



def all_pairwise_dist(points):
    allCombos = list(combinations(points, 2))
    pairwiseDist = {}
    for pair in allCombos:
        dist = euc_dist(pair[0], pair[1])
        pairwiseDist[dist] = (pair[0], pair[1])
    smallestDist = min(pairwiseDist.keys())
    return smallestDist, pairwiseDist[smallestDist]