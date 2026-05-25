

import unittest
from typing import List

from longest_common_prefix.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_prefix(self):
        self.assertEqual(self.solution.longestCommonPrefix(["flower","flow","flight"]), "fl")
        self.assertEqual(self.solution.longestCommonPrefix(["dog","racecar","car"]), "")
        self.assertEqual(self.solution.longestCommonPrefix(["ab","a"]), "a")


if __name__ == '__main__':
    unittest.main()