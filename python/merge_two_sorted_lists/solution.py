from typing import Optional, List
import copy

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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        t = self
        res=""
        while t:
            res+=str(t.val)
            t=t.next
        return res
    def __repr__(self):
        t = self
        res=""
        while t:
            res+=str(t.val)
            t=t.next
        return res
    
    def __eq__(self, value):
        if not isinstance(value, ListNode):
            return False
        t1 = self
        t2 = value
        while t1 and t2:
            if t1.val != t2.val:
                return False
            t1 = t1.next
            t2 = t2.next
        return not t1 and not t2
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = last_node = ListNode()
        
        while list1 or list2:
            if list1 and list2 and list1.val < list2.val or (list1 and not list2):
                last_node.next = list1
                list1 = list1.next
            else:
                last_node.next = list2
                list2 = list2.next
            last_node = last_node.next

        return head.next
            
                

if __name__ == "__main__":
    solution = Solution()

    l1 =  createList([1,2,3,4,5])
    l2 =  createList([1,2,3,4,5])
    print(solution.mergeTwoLists(l1,l2))
