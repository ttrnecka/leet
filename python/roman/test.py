

import unittest
from typing import List

from roman.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_is_match(self):
        self.assertEqual(self.solution.intToRoman(3), "III")
        self.assertEqual(self.solution.intToRoman(4), "IV")
        self.assertEqual(self.solution.intToRoman(58), "LVIII")
        self.assertEqual(self.solution.intToRoman(3749), "MMMDCCXLIX")

if __name__ == '__main__':
    unittest.main()