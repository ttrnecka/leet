

import unittest
from typing import List

from longest_valid_parentheses.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution() 
    
    def test_longestValidParentheses(self):
        s = "(()"
        self.assertEqual(self.solution.longestValidParentheses(s), 2)

        s = ")()())"
        self.assertEqual(self.solution.longestValidParentheses(s), 4)

        s = ""
        self.assertEqual(self.solution.longestValidParentheses(s), 0)


if __name__ == '__main__':
    unittest.main()