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
    n = len(searchList)
    stop1 = time.time()
    for t in range(-10000, 10001):
        if t % 100 == 0:
            print("-- %s took %s seconds --" % (t, (time.time() - stop1)))
            stop1 = time.time()
        for x in searchList:
            if t - x <= x:
                break
            i = bisect_left(searchList, t - x, hi=n-1)
            if searchList[i] == t - x:
                count += 1
                break
    return count



if __name__ == "__main__":
    startTime = time.time()
    l = sort_ints("prob6.txt")
    ans = count_targets(l)
    print("--- took %s seconds ---" % (time.time() - startTime))
    print("the answer is", ans)
