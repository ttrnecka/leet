

import unittest
from typing import List

from merge_two_sorted_lists.solution import Solution, ListNode

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_is_match(self):
        l1 =  createList([1,2,4])
        l2 =  createList([1,3,4])
        tl = createList([1,1,2,3,4,4])
        self.assertEqual(self.solution.mergeTwoLists(l1,l2), tl)

        l1 =  createList([])
        l2 =  createList([])
        tl = createList([])
        self.assertEqual(self.solution.mergeTwoLists(l1,l2), tl)

        l1 =  createList([])
        l2 =  createList([0])
        tl = createList([0])
        self.assertEqual(self.solution.mergeTwoLists(l1,l2), tl)


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