

import unittest
from typing import List

from search_in_rotated_sorted_array.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_search(self):
        self.assertEqual(self.solution.search([4,5,6,7,0,1,2], 0), 4)
        self.assertEqual(self.solution.search([4,5,6,7,0,1,2], 3), -1)
        self.assertEqual(self.solution.search([4,5,6,7,0,1,2], 6), 2)
        self.assertEqual(self.solution.search([1], 1), 0)
        self.assertEqual(self.solution.search([1], 2), -1)
        self.assertEqual(self.solution.search([1,3], 0), -1)

if __name__ == '__main__':
    unittest.main()