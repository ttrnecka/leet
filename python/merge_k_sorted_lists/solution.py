from typing import Optional, List
import heapq

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


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                sorted = self.mergeTwoLists(l1,l2)
                temp.append(sorted)
            lists = temp
        
        return lists[0]
    
    def mergeKListsHeap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        non_empty_lists = [list for list in lists if list]
        heap = []
        for i, node in enumerate(non_empty_lists):
            heapq.heappush(heap,(node.val, i, node))

        head = ListNode()
        current = head

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap,(node.next.val, i, node.next))
            
        return head.next

if __name__ == "__main__":
    solution = Solution()

    l1 =  createList([1,2,3,4,5])
    l2 =  createList([1,2,3,4,5])
    l3 =  createList([1,2,4,5])
    print(solution.mergeKLists([l1,l2,l3]))
    l1 =  createList([1,2,3,4,5])
    l2 =  createList([1,2,3,4,5])
    l3 =  createList([1,2,4,5])
    print(solution.mergeKListsHeap([l1,l2,l3]))
