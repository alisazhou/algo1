import time
from bisect import bisect_left


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
    count = 0
    targets = {}
    indX = 0
    for x in searchList:
        # use binary search to find index of (-10000 - x), lo
        lo = bisect_left(searchList, -10000 - x)
        # set index start to the greater of either lo or x's index + 1 (excl x)
        startInd = max(lo, indX + 1)

        # from start, go up elems in searchList, until elem > 10000 - x
        for elem in searchList[startInd:]:
            if elem > 10000 - x:
                break
            # check if elem + x is in targets, if not, add to targets
            target = elem + x
            if target in targets:
                continue
            else:
                count += 1
                targets[target] = count
        indX += 1

    return count



if __name__ == "__main__":
    startTime = time.time()
    l = sort_ints("prob6.txt")
    ans = count_targets(l)
    print("--- took %s seconds ---" % (time.time() - startTime))
    print("the answer is", ans)
