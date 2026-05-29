

import unittest
from typing import List

from remove_element.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
     
    def test_remove_element(self):
        nums = [1,1,2]
        expectedNums = [2]
        l = self.solution.removeElement(nums, 1)
        self.assertEqual(l, 1)
        for i in range(l):
            assert nums[i] == expectedNums[i]

        nums = [0,0,1,1,1,2,2,3,3,4]
        expectedNums = [0,0,2,2,3,3,4]
        l = self.solution.removeElement(nums, 1)
        self.assertEqual(l, 7)
        for i in range(l):
            assert nums[i] == expectedNums[i]

        nums = []
        expectedNums = []
        l = self.solution.removeElement(nums, 1)
        self.assertEqual(l, 0)
        for i in range(l):
            assert nums[i] == expectedNums[i]

if __name__ == '__main__':
    unittest.main()