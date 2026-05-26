

import unittest
from typing import List

from valid_parentheses.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_is_valid(self):
        self.assertEqual(self.solution.isValid("()"), True)
        self.assertEqual(self.solution.isValid("(]"), False)
        self.assertEqual(self.solution.isValid("([)]"), False)
        self.assertEqual(self.solution.isValid("()[]{}"), True)

if __name__ == '__main__':
    unittest.main()