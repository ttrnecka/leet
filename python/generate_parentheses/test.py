

import unittest
from typing import List

from generate_parentheses.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_is_match(self):
        self.assertEqual(self.solution.generateParenthesis(3), ["((()))","(()())","(())()","()(())","()()()"])

if __name__ == '__main__':
    unittest.main()