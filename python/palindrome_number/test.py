

import unittest
from typing import List

from palindrome_number.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_isPalindrome(self):
        self.assertEqual(self.solution.isPalindrome(42), False)
        self.assertEqual(self.solution.isPalindrome(121), True)
        self.assertEqual(self.solution.isPalindrome(-121), False)
        self.assertEqual(self.solution.isPalindrome(101010), False)
        self.assertEqual(self.solution.isPalindrome(10101), True)


if __name__ == '__main__':
    unittest.main()