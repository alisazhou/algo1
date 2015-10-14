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



def quicksort(toSort):
    n = len(toSort)
    if n <= 1:
        return toSort
    else:
        pivot = toSort[0]
        i = 1
        
    return toSort