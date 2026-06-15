from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        prev = None

        while fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next
            if fast.next:
                fast = fast.next

        # prev is just before the middle
        if not prev:
            return None

        prev.next = slow.next if slow else None

        return head
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.deleteMiddle(ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))))