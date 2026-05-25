

import unittest
from typing import List

from three_sums.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_three_sum(self):
        self.assertEqual(sorted(self.solution.threeSum([-1,0,1,2,-1,-4])), sorted([[-1, 0, 1], [-1, -1, 2]]))
        self.assertEqual(self.solution.threeSum([0,1,1]), [])
        self.assertEqual(self.solution.threeSum([0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(self.solution.threeSum([-1,0,1,0]), [[-1,0,1]])
        self.assertEqual(self.solution.threeSum([-2,0,1,1,2]), [[-2,0,2],[-2,1,1]])


if __name__ == '__main__':
    unittest.main()