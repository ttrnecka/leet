from search_in_rotated_sorted_array.solution import Solution
from benchmark import benchmark

class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, nums):
        self.solution.search(nums, 0)

print(Benchmark().test([4,5,6,7,0,1,2]))