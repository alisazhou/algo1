import time

def hash_ints(file_ints):
    """Insert all integers in the file into a hash table.
    
    Data file is an array of integers, one in each row.  Read file,
    insert into hash table, duplicates are removed in the process.
    Return the hash table of unique integers.
    """
    hashedInts = {}
    with open(file_ints) as f:
        i = 0
        for line in f:
            k = int(line)
            hashedInts[k] = i
            i += 1
    return hashedInts

def count_targets(hashedInts):
    count = 0
    stop1 = time.time()
    for t in range(-10000, 10001):
        if t % 100 == 0:
            print("--- %s seconds ---" % (time.time() - stop1))
            stop1 = time.time()
        for k in hashedInts:
            if (t - k) in hashedInts and (t - k) != k:
                count += 1
                break
    return count



if __name__ == "__main__":
    startTime = time.time()
    d = hash_ints("prob6.txt")
    ans = count_targets(d)
    print("------- %s seconds in total -------" % (time.time() - startTime))
    print("the answer is", ans)
