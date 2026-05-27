

import unittest
from typing import List

from merge_k_sorted_lists.solution import Solution, ListNode

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_is_match(self):
        l1 =  createList([1,2,4])
        l2 =  createList([1,3,4])
        l3 =  createList([1,3,4])
        tl = createList([1,1,1,2,3,3,4,4,4])
        self.assertEqual(self.solution.mergeKLists([l1, l2, l3]), tl)
        l1 =  createList([1,2,4])
        l2 =  createList([1,3,4])
        l3 =  createList([1,3,4])
        tl = createList([1,1,1,2,3,3,4,4,4])
        self.assertEqual(self.solution.mergeKListsHeap([l1, l2, l3]), tl)


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