def merge_sort(unsorted):
    n = len(unsorted)
    if n <= 1:
        return unsorted
    else:
        mid = n // 2
        sortedL = merge_sort(unsorted[:mid])
        sortedR = merge_sort(unsorted[mid:])
        sorted = merge(sortedL, sortedR)
        return sorted


def merge(left, right):
    sorted = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    if i < len(left):
        sorted += left[i:]
    elif j < len(right):
        sorted += right[j:]
    return sorted




def select_sort(unsorted):
    sorted = []
    while unsorted:
        smallest = unsorted[0]
        indexSmallest = 0
        for i in range(1, len(unsorted)):
            if unsorted[i] < smallest:
                smallest = unsorted[i]
                indexSmallest = i
        sorted.append(smallest)
        unsorted.pop(indexSmallest)
    return sorted




def insert_sort(unsorted):
    if unsorted == []:
        return unsorted
    else:
        sorted = [unsorted.pop()]
        while unsorted:
            next = unsorted.pop()
            for i in range(len(sorted)):
                if next < sorted[i]:
                    sorted.insert(i, next)
                    break
                if i == len(sorted) - 1:
                    sorted.append(next)
    return sorted




def bubble_sort(toSort):
    for n in range(len(toSort)):
        i, j = 0, 1
        while j < len(toSort):
            if toSort[i] > toSort[j]:
                toSort[i], toSort[j] = toSort[j], toSort[i]
            i += 1
            j += 1
    return toSort


compsFirst = 0
def quicksort_first(toSort):
    n = len(toSort)
    global compsFirst
    if n <= 1:
        return toSort
    else:
        pivot = toSort[0]
        toSort, p = partition(toSort)
        left = quicksort_first(toSort[:p])
        compsFirst += p - 1
        right = quicksort_first(toSort[p+1:])
        compsFirst += n - p
    sorted = left + right
    sorted.insert(p, pivot)
    return sorted

def partition(aList):
    pivot = aList[0]
    i = 1
    j = 1
    for elem in aList[1:]:
        if elem > pivot:
            j += 1
        else:
            aList[i], aList[j] = aList[j], aList[i]
            i += 1
            j += 1
    aList[0], aList[i-1] = aList[i-1], aList[0]
    return aList, i-1

compsLast = 0
def quicksort_last(toSort):
    n = len(toSort)
    global compsLast
    if n <= 1:
        return toSort
    else:
        toSort[0], toSort[-1] = toSort[-1], toSort[0]
        pivot = toSort[0]
        toSort, p = partition(toSort)
        left = quicksort_last(toSort[:p])
        compsLast += p - 1
        right = quicksort_last(toSort[p+1:])
        compsLast += n - p
    sorted = left + right
    sorted.insert(p, pivot)
    return sorted

compsMedian = 0
def quicksort_median(toSort):
    n = len(toSort)
    global compsMedian
    if n <= 1:
        return toSort
    else:
        mid = (n+1)//2 - 1
        if toSort[0] < toSort[-1]:
            if toSort[mid] < toSort[0]:
                p = 0
            elif toSort[mid] > toSort[-1]:
                p = -1
            else:
                p = mid
        else:
            if toSort[mid] > toSort[0]:
                p = 0
            elif toSort[mid] < toSort[-1]:
                p = -1
            else:
                p = mid
        
        toSort[0], toSort[p] = toSort[p], toSort[0]
        pivot = toSort[0]
        toSort, p = partition(toSort)
        left = quicksort_median(toSort[:p])
        compsMedian += p - 1
        right = quicksort_median(toSort[p+1:])
        compsMedian += n - p
    sorted = left + right
    sorted.insert(p, pivot)
    return sorted
            
    