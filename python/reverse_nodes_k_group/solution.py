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
        i=0
        while t and i<3:
            res+=str(t.val)
            t=t.next
            i+=1
        if i == 3 and t.next:
            res+="..."
        return res
    def __repr__(self):
        return self.__str__()
    
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
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            temp = group_prev
            for _ in range(k):
                temp = temp.next
                if not temp:
                    return dummy.next
            group_next = temp.next

            prev, curr = group_next, group_prev.next

            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            group_prev.next, group_prev = temp, group_prev.next

                

if __name__ == "__main__":
    solution = Solution()

    l =  createList([1,2,3,4,5])
    print(solution.reverseKGroup(l,2))
    l =  createList([1,2,3,4,5])
    print(solution.reverseKGroup(l,3))
    l =  createList([1,2,3,4])
    print(solution.reverseKGroup(l,4))