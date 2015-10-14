total = 0

def sort_and_count(lista):
    """
    Takes a list of int in random order, returns the number of inversions.
    
    Divide the list into two, recursively sort and count both halves, and merge them.
    While merging, keep running count of number of inversions.
    """
    
    if len(lista) < 2:
        return (lista, 0)
    else:
        k = len(lista) // 2
        left, totalLeft = sort_and_count(lista[:k])
        right, totalRight = sort_and_count(lista[k:])
        total = totalLeft + totalRight
        return merge_and_count(left, right, total)



def merge_and_count(listb, listc, total):
    listd = []
    i = 0
    j = 0
    m = len(listb)
    n = len(listc)
    while i < m and j < n:
        if listb[i] < listc[j]:
            listd.append(listb[i])
            i += 1
        else:
            total += m - i
            listd.append(listc[j])
            j += 1
    if i == m:
        listd += listc[j:]
    elif j == n:
        listd += listb[i:]
    return (listd, total)