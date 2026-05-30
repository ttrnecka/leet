

import unittest
from typing import List

from next_permutation.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution() 
    
    def test_nextPermutation(self):
        nums = [1, 2, 3]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [1, 3, 2])

        nums = [1, 3, 2]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, [2, 1, 3])

if __name__ == '__main__':
    unittest.main()