from max_ice_cream.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, costs, coins):
        self.solution.maxIceCream(costs, coins)

print(Benchmark().test([1,3,2,4], 7))