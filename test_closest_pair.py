import unittest
import closest_pair

class ClosestPairTest(unittest.TestCase):
    
    def test_euclidean_distance(self):
        output = closest_pair.euc_dist((0, 0), (1, 1))
        answer = 1.414214
        self.assertAlmostEqual(output, answer, places=5)
    
    def test_three_point_set_dist(self):
        input = [(-4, 1), (0, 0), (1, 1)]
        output = closest_pair.find_closest(input)
        dist = 1.414214
        pair = [(0, 0), (1, 1)]
        self.assertAlmostEqual(output[0], dist, places=5)
        self.assertEqual(set(output[1]), set(pair))
    
    def test_can_find_closest_pair(self):
        input = [(0, 0.51), (1.12, 0)]
        output = closest_pair.find_closest(input)[1]
        answer = [(0, 0.51), (1.12, 0)]
        self.assertEqual(set(output), set(answer))
    
    def test_can_find_closest_pair2(self):
        input = [(123, 15), (158, 12), (1859, -1489)]
        output = closest_pair.find_closest(input)[1]
        answer = [(123, 15), (158, 12)]
        self.assertEqual(set(output), set(answer))
    
    def test_can_find_closest_pair3(self):
        input = [(-7, -2), (-4, 1), (0, 0), (1, 1), (3, 3), (5, 5), (7, 7), (9, 9), (11, 11)]
        output = closest_pair.find_closest(input)[1]
        answer = [(0, 0), (1, 1)]
        self.assertEqual(set(output), set(answer))
    

if __name__ == '__main__':
    unittest.main()