

import unittest
from typing import List

from four_sums.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_four_sum(self):
        self.assertEqual(self.solution.fourSum([1, 0, -1, 0, -2, 2], 0), {(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)})
        self.assertEqual(self.solution.fourSum([2, 2, 2, 2, 2], 8), {(2, 2, 2, 2)})

if __name__ == '__main__':
    unittest.main()