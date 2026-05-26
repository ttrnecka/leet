from merge_two_sorted_lists.solution import Solution, createList
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, nums1, nums2):
        l1 = createList(nums1)
        l2 = createList(nums2)
        self.solution.mergeTwoLists(l1, l2)

print(Benchmark().test([1,2,3,4,5], [1,2,3,4,5]))