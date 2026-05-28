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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        while curr.next:
            hold = [None] *k 
            temp = curr
            for i in range(k):
                hold[i]=temp.next
                temp = temp.next
                if not temp:
                    return dummy.next
            
            for i in range(k // 2):
                if i!=k-i-1:
                    hold[i].next = hold[k-i-1]
                    hold[k-i-1].next = hold[i]

            curr.next = hold[0]

            curr = hold[k-1]

        return dummy.next
                

if __name__ == "__main__":
    solution = Solution()

    l =  createList([1,2,3,4,5])
    print(solution.reverseKGroup(l,2))
    l =  createList([1,2,3,4,5])
    print(solution.reverseKGroup(l,3))