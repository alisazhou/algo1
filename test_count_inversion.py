import unittest
import count_inversion

class InversionCountTest(unittest.TestCase):

    def test_can_sort_a_list(self):
        unsorted_list = [1, 3, 5, 2, 4, 6]
        returned_list = count_inversion.sort_and_count(unsorted_list)[0]
        sorted_list = sorted(unsorted_list)
        self.assertEqual(returned_list, sorted_list)
    
    def test_can_merge_a_list(self):
        listb = [1, 3, 5]
        listc = [2, 4, 6]
        merged_list = count_inversion.merge_and_count(listb, listc, 0)[0]
        lista = listb + listc
        lista.sort()
        self.assertEqual(merged_list, lista)
    
    def test_can_count_while_merging(self):
        listb = [1, 3, 5]
        listc = [2, 4, 6]
        inversion_merged = count_inversion.merge_and_count(listb, listc, 0)[1]
        self.assertEqual(inversion_merged, 3)
        
    def test_base_case(self):
        singleton_list = [5]
        inversion_count = count_inversion.sort_and_count(singleton_list)[1]
        self.assertEqual(inversion_count, 0)
    
    def test_final_count(self):
        unsorted_list = [1, 3, 5, 2, 4, 6]
        returned_count = count_inversion.sort_and_count(unsorted_list)[1]
        self.assertEqual(returned_count, 3)

    def test_final_count2(self):
        unsorted_list = [2, 4, 1, 3, 5]
        returned_count = count_inversion.sort_and_count(unsorted_list)[1]
        self.assertEqual(returned_count, 3)

    def test_final_count(self):
        unsorted_list = [6, 5, 4, 3, 2, 1]
        returned_count = count_inversion.sort_and_count(unsorted_list)[1]
        self.assertEqual(returned_count, 15)		


if __name__ == '__main__':
    unittest.main()