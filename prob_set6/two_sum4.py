import time
from bisect import bisect_left, bisect_right


def sort_ints(file_ints):
    """Read integers from file and return a sorted array of the integers.

    Data file is an array of integers, one in each row.  Read file, omit
    duplicates, insert into list, sort list.
    """
    intListDupes = []
    with open(file_ints) as f:
        for line in f:
            intListDupes.append(int(line))
    intListUniq = list(set(intListDupes))
    intListUniq.sort()
    return intListUniq



def count_targets(searchList):
    """Count obtainable targets from summing up two ints from input list.

    For each target sum t in range [-10000, 10000], for each x in sorted
    array of integers, do a binary search in array for integer (t - x). 
    Return count of possible target sums.
    """
    targets = {}
    for x in searchList:
        loVal = -10000 - x
        hiVal = 10000 - x
        loInd = bisect_left(searchList, loVal)
        hiInd = bisect_right(searchList, hiVal)
        for y in searchList[loInd:hiInd]:
            if y == x:
                continue
            t = x + y
            targets[t] = 1
    return len(targets)
    




if __name__ == "__main__":
    startTime = time.time()
    l = sort_ints("prob6.txt")
    ans = count_targets(l)
    print("--- took %s seconds ---" % (time.time() - startTime))
    print("the answer is", ans)
