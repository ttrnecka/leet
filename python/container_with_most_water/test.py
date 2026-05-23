

import unittest
from typing import List

from container_with_most_water.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_maxarea(self):
        self.assertEqual(self.solution.maxArea([1,8,6,2,5,4,8,3,7]),49)


if __name__ == '__main__':
    unittest.main()