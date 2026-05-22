
from typing import Optional

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list = ListNode()
        plist = list
        move = 0
        while True:
            val = move
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            remainder = val % 10
            move = val // 10
            plist.val = remainder
            if not l1 and not l2 and move == 0:
                break
            plist.next = ListNode()
            plist = plist.next
        return list
        
        

if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(2,ListNode(3,ListNode(4)))
    l2 = ListNode(5,ListNode(7,ListNode(4)))
    # s = solution.addTwoNumbers(l1,l2)
    print(solution.addTwoNumbers(l1,l2))
    