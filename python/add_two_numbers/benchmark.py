from add_two_numbers.solution import Solution, ListNode
from add_two_numbers.test import createLinkedList
from benchmark import benchmark


class TestAddTwoNumbers:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, l1, l2):
        self.solution.addTwoNumbers(l1, l2)

l1 = createLinkedList([2, 4, 3])
l2 = createLinkedList([5, 6, 4])
test = TestAddTwoNumbers()
print(test.test(l1, l2))