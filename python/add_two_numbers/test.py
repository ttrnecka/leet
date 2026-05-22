

import unittest
from typing import List

from add_two_numbers.solution import Solution, ListNode

class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_add_two_numbers(self):
        l1 = createLinkedList([2, 4, 3])
        l2 = createLinkedList([5, 6, 4])
        self.assertEqual(self.solution.addTwoNumbers(l1, l2), createLinkedList([7, 0, 8]))
        self.assertEqual(self.solution.addTwoNumbers(createLinkedList([0]), createLinkedList([0])), createLinkedList([0]))
        self.assertEqual(self.solution.addTwoNumbers(createLinkedList([9, 9, 9, 9, 9, 9, 9]), createLinkedList([9, 9, 9, 9])), createLinkedList([8, 9, 9, 9, 0, 0, 0, 1]))


def createLinkedList(nums: List[int]) -> ListNode:
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head
if __name__ == '__main__':
    unittest.main()