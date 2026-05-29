from needle_in_haystack.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, haystack, needle):
        self.solution.strStr(haystack, needle)

print(Benchmark().test("saedbutsad", "sad"))
