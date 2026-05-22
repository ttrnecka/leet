

import unittest
from typing import List

from longest_nonrepeating_substring.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_lengthOfLongestSubstring(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)


if __name__ == '__main__':
    unittest.main()