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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        q = []
        r_head = head
        if head is None:
            return None
        while head:
            q.append(head)
            if len(q) > n+1:
                q.pop(0)
            head = head.next


        if len(q) > 2:
            if n == len(q):
                # removing first
                r_head = q.pop(1)
            else:
                nl = q.pop(0)
                nr = q.pop(1)
                nl.next = nr
        # removing first Node, returning rest
        elif len(q) == 2 and n == 2:
            r_head = q.pop(1)
        # removing last Node, returning head
        elif len(q) == 2 and n == 1:
            prev = q.pop(0)
            prev.next = None
        else:
            return None
        return r_head
                

if __name__ == "__main__":
    solution = Solution()

    l =  createList([1,2,3,4,5])
    print(solution.removeNthFromEnd(l,2))
    l =  createList([1,2])
    print(solution.removeNthFromEnd(l,1))