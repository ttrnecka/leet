from count_and_say.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, n):
        self.solution.countAndSay(n)

print(Benchmark().test(4))