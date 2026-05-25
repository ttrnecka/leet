

import unittest
from typing import List

from three_sums_closest.solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_three_sum(self):
        self.assertEqual(self.solution.threeSumClosest([-1,2,1,-4],1), 2)
        self.assertEqual(self.solution.threeSumClosest([0,0,0],1), 0)
        self.assertEqual(self.solution.threeSumClosest([4,0,5,-5,3,3,0,-4,-5],-2), -2)
        self.assertEqual(self.solution.threeSumClosest([10,20,30,40,50,60,70,80,90],1), 60)

if __name__ == '__main__':
    unittest.main()