from merge_k_sorted_lists.solution import Solution, createList
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, nums1, nums2, nums3):
        l1 = createList(nums1)
        l2 = createList(nums2)
        l3 = createList(nums3)
        self.solution.mergeKLists([l1, l2, l3])
    @benchmark(repeats=100)
    def testHeap(self, nums1, nums2, nums3):
        l1 = createList(nums1)
        l2 = createList(nums2)
        l3 = createList(nums3)
        self.solution.mergeKListsHeap([l1, l2, l3])

print(Benchmark().test([1,2,3,4,5], [1,2,3,4,5], [1,3,4]))
print(Benchmark().testHeap([1,2,3,4,5], [1,2,3,4,5], [1,3,4]))