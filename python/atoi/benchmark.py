from atoi.solution import Solution
from benchmark.main import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, s):
        self.solution.myAtoi(s)

print(Benchmark().test("42"))