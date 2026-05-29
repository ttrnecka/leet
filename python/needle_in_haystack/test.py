

import unittest
from typing import List

from needle_in_haystack.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_is_match(self):
        self.assertEqual(self.solution.strStr("sadbutsad", "sad"), 0)
        self.assertEqual(self.solution.strStr("leetcode", "leeto"), -1)

if __name__ == '__main__':
    unittest.main()