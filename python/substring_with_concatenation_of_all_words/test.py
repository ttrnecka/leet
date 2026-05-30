

import unittest
from typing import List

from substring_with_concatenation_of_all_words.solution import Solution
 
class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_findSubstring(self):
        self.assertEqual(self.solution.findSubstring("barfoothefoobarman", ["foo", "bar"]), [0, 9])

if __name__ == '__main__':
    unittest.main()