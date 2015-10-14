import unittest, sorting


class MergeSortTest(unittest.TestCase):

    def test_case_even(self):
        unsorted = [1, 3, 5, 7, 2, 4, 6, 8]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.merge_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_odd(self):
        unsorted = [1, 3, 5, 7, 2, 4, 6]
        sorted = [1, 2, 3, 4, 5, 6, 7]
        result = sorting.merge_sort(unsorted)
        self.assertEqual(result, sorted)
    
    def test_case_sorted(self):
        unsorted = [1, 2, 3, 4, 5, 6, 7, 8]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.merge_sort(unsorted)
        self.assertEqual(result, sorted)
    
    def test_case_empty(self):
        unsorted = []
        sorted = []
        result = sorting.merge_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_reverse(self):
        unsorted = [8, 7, 6, 5, 4, 3, 2, 1]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.merge_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_dupes(self):
        unsorted = [1, 3, 3, 5, 7, 2, 4, 6, 6, 8]
        sorted = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8]
        result = sorting.merge_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_same(self):
        unsorted = [1, 1, 1, 1]
        sorted = [1, 1, 1, 1]
        result = sorting.merge_sort(unsorted)
        self.assertEqual(result, sorted)


class SelectionSortTest(unittest.TestCase):
    
    def test_case_even(self):
        unsorted = [1, 3, 5, 7, 2, 4, 6, 8]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.select_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_odd(self):
        unsorted = [1, 3, 5, 7, 2, 4, 6]
        sorted = [1, 2, 3, 4, 5, 6, 7]
        result = sorting.select_sort(unsorted)
        self.assertEqual(result, sorted)
    
    def test_case_sorted(self):
        unsorted = [1, 2, 3, 4, 5, 6, 7, 8]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.select_sort(unsorted)
        self.assertEqual(result, sorted)
    
    def test_case_empty(self):
        unsorted = []
        sorted = []
        result = sorting.select_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_reverse(self):
        unsorted = [8, 7, 6, 5, 4, 3, 2, 1]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.select_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_dupes(self):
        unsorted = [1, 3, 3, 5, 7, 2, 4, 6, 6, 8]
        sorted = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8]
        result = sorting.select_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_same(self):
        unsorted = [1, 1, 1, 1]
        sorted = [1, 1, 1, 1]
        result = sorting.select_sort(unsorted)
        self.assertEqual(result, sorted)
        


class InsertionSortTest(unittest.TestCase):

    def test_case_even(self):
        unsorted = [1, 3, 5, 7, 2, 4, 6, 8]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.insert_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_odd(self):
        unsorted = [1, 3, 5, 7, 2, 4, 6]
        sorted = [1, 2, 3, 4, 5, 6, 7]
        result = sorting.insert_sort(unsorted)
        self.assertEqual(result, sorted)
    
    def test_case_sorted(self):
        unsorted = [1, 2, 3, 4, 5, 6, 7, 8]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.insert_sort(unsorted)
        self.assertEqual(result, sorted)
    
    def test_case_empty(self):
        unsorted = []
        sorted = []
        result = sorting.insert_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_reverse(self):
        unsorted = [8, 7, 6, 5, 4, 3, 2, 1]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.insert_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_dupes(self):
        unsorted = [1, 3, 3, 5, 7, 2, 4, 6, 6, 8]
        sorted = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8]
        result = sorting.insert_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_same(self):
        unsorted = [1, 1, 1, 1]
        sorted = [1, 1, 1, 1]
        result = sorting.insert_sort(unsorted)



class BubbleSortTest(unittest.TestCase):

    def test_case_even(self):
        unsorted = [1, 3, 5, 7, 2, 4, 6, 8]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.bubble_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_odd(self):
        unsorted = [1, 3, 5, 7, 2, 4, 6]
        sorted = [1, 2, 3, 4, 5, 6, 7]
        result = sorting.bubble_sort(unsorted)
        self.assertEqual(result, sorted)
    
    def test_case_sorted(self):
        unsorted = [1, 2, 3, 4, 5, 6, 7, 8]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.bubble_sort(unsorted)
        self.assertEqual(result, sorted)
    
    def test_case_empty(self):
        unsorted = []
        sorted = []
        result = sorting.bubble_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_reverse(self):
        unsorted = [8, 7, 6, 5, 4, 3, 2, 1]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.bubble_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_dupes(self):
        unsorted = [1, 3, 3, 5, 7, 2, 4, 6, 6, 8]
        sorted = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8]
        result = sorting.bubble_sort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_same(self):
        unsorted = [1, 1, 1, 1]
        sorted = [1, 1, 1, 1]
        result = sorting.bubble_sort(unsorted)


class QuickSortTest(unittest.TestCase):

    def test_case_even(self):
        unsorted = [1, 3, 5, 7, 2, 4, 6, 8]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.quicksort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_odd(self):
        unsorted = [1, 3, 5, 7, 2, 4, 6]
        sorted = [1, 2, 3, 4, 5, 6, 7]
        result = sorting.quicksort(unsorted)
        self.assertEqual(result, sorted)
    
    def test_case_sorted(self):
        unsorted = [1, 2, 3, 4, 5, 6, 7, 8]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.quicksort(unsorted)
        self.assertEqual(result, sorted)
    
    def test_case_empty(self):
        unsorted = []
        sorted = []
        result = sorting.quicksort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_reverse(self):
        unsorted = [8, 7, 6, 5, 4, 3, 2, 1]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sorting.quicksort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_dupes(self):
        unsorted = [1, 3, 3, 5, 7, 2, 4, 6, 6, 8]
        sorted = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8]
        result = sorting.quicksort(unsorted)
        self.assertEqual(result, sorted)

    def test_case_same(self):
        unsorted = [1, 1, 1, 1]
        sorted = [1, 1, 1, 1]
        result = sorting.quicksort(unsorted)


if __name__ == "__main__":
    unittest.main()