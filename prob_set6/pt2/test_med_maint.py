import unittest
import heapq
import med_maint


class ReadsFileTest(unittest.TestCase):

    def test_outputs_nums_from_file_in_order(self):
        inFile = "testcase1_54.txt"
        result = med_maint.read_file(inFile)
        answer = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
        self.assertEqual(result, answer)



class MaintainsHeapsTest(unittest.TestCase):

    def test_two_empty_heaps(self):
        inNum = 4
        hLo = []
        hHi = []
        resLo, resHi = med_maint.insert_num(inNum, hLo, hHi)[:2]
        self.assertEqual(resLo, hLo)
        self.assertEqual(resHi, [4])

    def test_single_and_empty_insert_to_lo(self):
        inNum = 4
        hLo = []
        hHi = [7]
        resLo, resHi = med_maint.insert_num(inNum, hLo, hHi, equalLen=False)[:2]
        ansLo = [-4]
        self.assertEqual(resLo, ansLo)
        self.assertEqual(resHi, hHi)

    def test_single_and_empty_insert_to_hi(self):
        inNum = 4
        hLo = []
        hHi = [3]
        resLo, resHi = med_maint.insert_num(inNum, hLo, hHi, equalLen=False)[:2]
        ansLo = [-3]
        ansHi = [4]
        self.assertEqual(resLo, ansLo)
        self.assertEqual(resHi, ansHi)

    def test_two_equal_len_insert_to_lo(self):
        inNum = 2
        hLo = [-1, -3]
        heapq.heapify(hLo)
        hHi = [4, 5]
        heapq.heapify(hHi)
        resLo, resHi = med_maint.insert_num(inNum, hLo, hHi)[:2]
        ansLo = [-1, -2]
        heapq.heapify(ansLo)
        ansHi = [3, 4, 5]
        heapq.heapify(ansHi)
        self.assertEqual(resLo, ansLo)
        while ansHi:
            self.assertEqual(heapq.heappop(resHi), heapq.heappop(ansHi))

    def test_two_equal_len_insert_to_hi(self):
        inNum = 5
        hLo = [-1, -2]
        heapq.heapify(hLo)
        hHi = [3, 4]
        heapq.heapify(hHi)
        resLo, resHi = med_maint.insert_num(inNum, hLo, hHi)[:2]
        ansHi = [3, 4, 5]
        heapq.heapify(ansHi)
        self.assertEqual(resLo, hLo)
        while ansHi:
            self.assertEqual(heapq.heappop(resHi), heapq.heappop(ansHi))

    def test_two_unequal_len_insert_to_lo(self):
        inNum = 2
        hLo = [-1]
        hHi = [3, 4]
        heapq.heapify(hHi)
        resLo, resHi = med_maint.insert_num(inNum, hLo, hHi, equalLen=False)[:2]
        ansLo = [-1, -2]
        heapq.heapify(ansLo)
        self.assertEqual(resLo, ansLo)
        self.assertEqual(resHi, hHi)

    def test_two_unequal_len_insert_to_hi(self):
        inNum = 4
        hLo = [-1]
        hHi = [2, 3]
        heapq.heapify(hHi)
        resLo, resHi = med_maint.insert_num(inNum, hLo, hHi, equalLen=False)[:2]
        ansLo = [-1, -2]
        heapq.heapify(ansLo)
        ansHi = [3, 4]
        heapq.heapify(ansHi)
        self.assertEqual(resLo, ansLo)
        self.assertEqual(resHi, ansHi)


    
class CalculatesMedianTest(unittest.TestCase):

    def test_two_empty_heaps(self):
        inNum = 4
        hLo = []
        hHi = []
        resMed = med_maint.insert_num(inNum, hLo, hHi)[-1]
        self.assertEqual(resMed, 4)

    def test_single_and_empty_insert_to_lo(self):
        inNum = 4
        hLo = []
        hHi = [7]
        resMed = med_maint.insert_num(inNum, hLo, hHi, equalLen=False)[-1]
        ansMed = 4
        self.assertEqual(resMed, ansMed)

    def test_single_and_empty_insert_to_hi(self):
        inNum = 4
        hLo = []
        hHi = [3]
        resMed = med_maint.insert_num(inNum, hLo, hHi, equalLen=False)[-1]
        ansMed = 3
        self.assertEqual(resMed, ansMed)

    def test_two_equal_len_insert_to_lo(self):
        inNum = 2
        hLo = [-1, -3]
        heapq.heapify(hLo)
        hHi = [4, 5]
        heapq.heapify(hHi)
        resMed = med_maint.insert_num(inNum, hLo, hHi)[-1]
        ansMed = 3
        self.assertEqual(resMed, ansMed)

    def test_two_equal_len_insert_to_hi(self):
        inNum = 5
        hLo = [-1, -2]
        heapq.heapify(hLo)
        hHi = [3, 4]
        heapq.heapify(hHi)
        resMed = med_maint.insert_num(inNum, hLo, hHi)[-1]
        ansMed = 3
        self.assertEqual(resMed, ansMed)

    def test_two_unequal_len_insert_to_lo(self):
        inNum = 2
        hLo = [-1]
        hHi = [3, 4]
        heapq.heapify(hHi)
        resMed = med_maint.insert_num(inNum, hLo, hHi, equalLen=False)[-1]
        ansMed = 2
        self.assertEqual(resMed, ansMed)

    def test_two_unequal_len_insert_to_hi(self):
        inNum = 4
        hLo = [-1]
        hHi = [2, 3]
        heapq.heapify(hHi)
        resMed = med_maint.insert_num(inNum, hLo, hHi, equalLen=False)[-1]
        ansMed = 2
        self.assertEqual(resMed, ansMed)

    def test_misc(self):
        inNum = 3
        hLo = [-1]
        hHi = [2]
        resMed = med_maint.insert_num(inNum, hLo, hHi)[-1]
        ansMed = 2
        self.assertEqual(resMed, ansMed)



class RecordsMedianTest(unittest.TestCase):

    def test_singleton_input(self):
        intStream = [4]
        resMeds = med_maint.record_medians(intStream)
        ansMeds = [4]
        self.assertEqual(resMeds, ansMeds)

    def test_mult_in_order(self):
        intStream = [1, 2, 3, 4]
        resMeds = med_maint.record_medians(intStream)
        ansMeds = [1, 1, 2, 2]
        self.assertEqual(resMeds, ansMeds)

    def test_mult_reverse_order(self):
        intStream = [4, 3, 2, 1]
        resMeds = med_maint.record_medians(intStream)
        ansMeds = [4, 3, 3, 2]
        self.assertEqual(resMeds, ansMeds)

    def test_random_order(self):
        intStream = [3, 1, 2, 4]
        resMeds = med_maint.record_medians(intStream)
        ansMeds = [3, 1, 2, 2]
        self.assertEqual(resMeds, ansMeds)




if __name__ == "__main__":
    unittest.main()
