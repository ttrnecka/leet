

import unittest
from typing import List

from remove_nth_node.solution import Solution, ListNode

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_is_match(self):
        l =  createList([1,2,3,4,5])
        tl = createList([1,2,3,5])
        self.assertEqual(self.solution.removeNthFromEnd(l,2), tl)

        l =  createList([1])
        tl = createList([])
        self.assertEqual(self.solution.removeNthFromEnd(l,1), tl)

        l =  createList([1,2])
        tl = createList([1])
        self.assertEqual(self.solution.removeNthFromEnd(l,1), tl)
       
        l =  createList([1,2,3])
        tl = createList([2,3])
        self.assertEqual(self.solution.removeNthFromEnd(l,3), tl)

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