

import unittest
from typing import List

from regexp.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_is_match(self):
        self.assertEqual(self.solution.isMatch("aa", "a"), False)
        self.assertEqual(self.solution.isMatch("aa", "aa"), True)
        self.assertEqual(self.solution.isMatch("aaa", "a*"), True)
        self.assertEqual(self.solution.isMatch("aa", "a."), True)
        self.assertEqual(self.solution.isMatch("ab", "a."), True)
        self.assertEqual(self.solution.isMatch("ab", "a*"), False)
        self.assertEqual(self.solution.isMatch("ab", ".*"), True)
        self.assertEqual(self.solution.isMatch("aab", "c*a*b"), True)
        self.assertEqual(self.solution.isMatch("aaa", "a*a"), True)


if __name__ == '__main__':
    unittest.main()