from remove_element.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, nums):
        self.solution.removeElement(nums, 1)

print(Benchmark().test([0,0,1,1,1,2,2,3,3,4]))