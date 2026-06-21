

import unittest
from typing import List

from count_and_say.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_count_and_say(self):
        self.assertEqual(self.solution.countAndSay(1), "1")
        self.assertEqual(self.solution.countAndSay(2), "11")
        self.assertEqual(self.solution.countAndSay(3), "21")
        self.assertEqual(self.solution.countAndSay(4), "1211")

if __name__ == '__main__':
    unittest.main()