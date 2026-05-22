from regexp.solution import Solution
from benchmark.main import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, s,p):
        self.solution.isMatch(s,p)

print(Benchmark().test("aaa","a*a"))