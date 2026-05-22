

import unittest
from typing import List

from sorted_array_median.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_findMedianSortedArrays(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1,3], [2]), 2.0)
        self.assertEqual(self.solution.findMedianSortedArrays([1,2], [3,4]), 2.5)


if __name__ == '__main__':
    unittest.main()