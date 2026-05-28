

import unittest
from typing import List

from remove_duplicates_from_array.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_remove_duplicates(self):
        nums = [1,1,2]
        expectedNums = [1,2]
        l = self.solution.removeDuplicates(nums)
        self.assertEqual(l, 2)
        for i in range(l):
            assert nums[i] == expectedNums[i]

        nums = [0,0,1,1,1,2,2,3,3,4]
        expectedNums = [0,1,2,3,4]
        l = self.solution.removeDuplicates(nums)
        self.assertEqual(l, 5)
        for i in range(l):
            assert nums[i] == expectedNums[i]

        nums = []
        expectedNums = []
        l = self.solution.removeDuplicates(nums)
        self.assertEqual(l, 0)
        for i in range(l):
            assert nums[i] == expectedNums[i]

if __name__ == '__main__':
    unittest.main()