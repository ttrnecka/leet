from reverse_nodes_k_group.solution import Solution, createList
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, nums):
        l =  createList(nums)
        self.solution.reverseKGroup(l, 2)

print(Benchmark().test([1,2,3,4,5]))