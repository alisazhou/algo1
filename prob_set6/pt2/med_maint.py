from heapq import heappop, heappush, heappushpop


def read_file(inFile):
    """Takes an input file of ints in str, output into list"""
    numsList = []
    with open(inFile) as f:
        for lineStr in f:
            numInt = int(lineStr)
            numsList.append(numInt)
    return numsList


def insert_num(num, heapLo, heapHi, equalLen=True):
    """Takes int, insert into correct heap, maintain balanced heaps."""
    # check if either of heaps are empty
    if heapHi == []: # heapLo is definitely empty also
        heapHi.append(num)
        return heapLo, heapHi, num
    elif heapLo == []:
        minOfLo = heappushpop(heapHi, num)
        heapLo = [-minOfLo]
        # again, contrary to mathematical def of median, use the smaller of the
        # middle two numbers as median, instead of average.  see below
        # maxOfHi = heapHi[0]
        # median = (minOfLo + maxOfHi) / 2
        median = minOfLo
        return heapLo, heapHi, median

    minOfHi = heappop(heapHi)
    maxOfLo = - (heappop(heapLo))    # heapLo are neg of actual ints

    if equalLen:
        heappush(heapHi, minOfHi)
        if num > maxOfLo:
            # insert num into heapHi, then get new minOfHi
            heappush(heapHi, num)
            heappush(heapLo, -maxOfLo)
            minOfHi = min(num, minOfHi)
        else:
            # insert num into heapLo, maxOfLo into heapHi, becomes new minOfHi
            heappush(heapHi, maxOfLo)
            heappush(heapLo, -num)
            minOfHi = maxOfLo
        median = minOfHi

    else:
        heappush(heapLo, -maxOfLo)
        if num < minOfHi:
            # insert minOfHi into heapHi,  num into heapLo, get new maxOfLo
            heappush(heapHi, minOfHi)
            maxOfLo = -(heappushpop(heapLo, -num))
            heappush(heapLo, -maxOfLo)
        else:
            # insert minOfHi into heapLo, minOfHi now is maxOfLo
            # insert num into heapHi, get new minOfHi
            # according to problem description, no need to get new minOfHi
            heappush(heapLo, -minOfHi)
            maxOfLo = minOfHi
            # minOfHi = heappushpop(heapHi, num)
            # heappush(heapHi, minOfHi)
            heappush(heapHi, num)
        # mathematically, it should be: median = (minOfHi + maxOfLo) / 2
        # however, according to definition in the problem description, return
        # median as the smaller of the middle two numbers instead
        median = maxOfLo

    return heapLo, heapHi, median


def record_medians(numsList):
    """Takes list of ints, returns list of medians as ints stream in."""
    heapLo = []
    heapHi = []
    medians = []
    count = 0
    for num in numsList:
        if count % 2 == 0:
            equalLen = True
        else:
            equalLen = False
        heapLo, heapHi, median = insert_num(num, heapLo, heapHi, equalLen)
        medians.append(median)
        count += 1
    return medians
        


def main(inFile):
    """Calculates the sum of medians given a stream of ints.

    Given a sequence of ints, as each input is read, maintain two heaps,
    one with the smaller half of the ints, the other the larger half.
    Maintain record of medians as ints stream in by getting the max of
    the lower half, and max of the upper half. Output the sum of the
    medians.
    """
    numsList = read_file(inFile)
    medians = record_medians(numsList)
    ans = sum(medians)
    return ans


if __name__ == "__main__":
    import time
    startTime = time.time()
    answer = main("prob6_2.txt") % 10000
    print("--- %s seconds ---" % (time.time() - startTime))
    print("sum of medians is:", answer)
