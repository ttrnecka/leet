

import unittest
from typing import List

from divide_two_integers.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_divide(self):
        self.assertEqual(self.solution.divide(10, 3), 3)
        self.assertEqual(self.solution.divide(7, -3), -2)

if __name__ == '__main__':
    unittest.main()