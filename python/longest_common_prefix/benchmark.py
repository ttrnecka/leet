from longest_common_prefix.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, l):
        self.solution.longestCommonPrefix(l)

print(Benchmark().test(["flower","flow","flight"]))