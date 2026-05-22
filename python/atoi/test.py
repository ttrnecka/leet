

import unittest
from typing import List

from atoi.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_atoi(self):
        self.assertEqual(self.solution.myAtoi("42"), 42)
        self.assertEqual(self.solution.myAtoi("   -42"), -42)
        self.assertEqual(self.solution.myAtoi("4193 with words"), 4193)
        self.assertEqual(self.solution.myAtoi("words and 987"), 0)
        self.assertEqual(self.solution.myAtoi("-91283472332"), -2147483648)
        self.assertEqual(self.solution.myAtoi("91283472332"), 2147483647)


if __name__ == '__main__':
    unittest.main()