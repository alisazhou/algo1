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
    targets = []
    for k in hashedInts:
        
    return count
