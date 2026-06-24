

import unittest
from typing import List

from multiply_strings.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_multiply(self):
        self.assertEqual(self.solution.multiply("2", "3"), "6")
        self.assertEqual(self.solution.multiply("123", "456"), "56088")


if __name__ == '__main__':
    unittest.main()