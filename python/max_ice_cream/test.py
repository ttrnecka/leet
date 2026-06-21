

import unittest
from typing import List

from max_ice_cream.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_max_ice_cream(self):
        self.assertEqual(self.solution.maxIceCream([1,3,2,4], 7), 3)
        self.assertEqual(self.solution.maxIceCream([10,6,8,7,7,8], 5), 0)
        self.assertEqual(self.solution.maxIceCream([5,6,7,8,9], 20), 3)
        self.assertEqual(self.solution.maxIceCream([1,6,3,1,2,5], 20), 6)

if __name__ == '__main__':
    unittest.main()