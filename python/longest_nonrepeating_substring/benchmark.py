from longest_nonrepeating_substring.solution import Solution
from benchmark.main import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, s):
        self.solution.lengthOfLongestSubstring(s)

print(Benchmark().test("abcabcbb"))