

import unittest
from typing import List

from reverse_nodes_k_group.solution import Solution, ListNode

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_is_match(self):
        l =  createList([1,2,3,4,5])
        tl = createList([3,2,1,4,5])
        self.assertEqual(self.solution.reverseKGroup(l, 3), tl)

        l =  createList([1])
        tl = createList([1])
        self.assertEqual(self.solution.reverseKGroup(l, 1), tl)

        l =  createList([1,2])
        tl = createList([2,1])
        self.assertEqual(self.solution.reverseKGroup(l, 2), tl)

def createList(nums: List):
    first_node = None
    previous_node = None
    for n in nums:
        node = ListNode(n)
        if not first_node:
            first_node = node
        if previous_node:
            previous_node.next = node
        previous_node = node
    return first_node
        

if __name__ == '__main__':
    unittest.main()