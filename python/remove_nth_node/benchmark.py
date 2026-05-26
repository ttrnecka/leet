from remove_nth_node.solution import Solution, createList
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, nums, n):
        l =  createList(nums)
        self.solution.removeNthFromEnd(l,n)

print(Benchmark().test([1,2,3,4,5],2))