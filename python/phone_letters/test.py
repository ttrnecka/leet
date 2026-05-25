

import unittest
from typing import List

from phone_letters.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_three_sum(self):
        self.assertEqual(self.solution.letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])
        self.assertEqual(self.solution.letterCombinations("2"), ["a","b","c"])


if __name__ == '__main__':
    unittest.main()