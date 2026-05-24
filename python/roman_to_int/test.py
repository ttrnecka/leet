

import unittest
from typing import List

from roman_to_int.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_is_match(self):
        self.assertEqual(self.solution.romanToInt("III"), 3)
        self.assertEqual(self.solution.romanToInt("IV"), 4)
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)
        self.assertEqual(self.solution.romanToInt("MMMDCCXLIX"), 3749)

if __name__ == '__main__':
    unittest.main()