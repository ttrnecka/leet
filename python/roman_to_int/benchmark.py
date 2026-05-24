from roman_to_int.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, s):
        self.solution.romanToInt(s)
    @benchmark(repeats=100)
    def test2(self, s):
        self.solution.romanToInt2(s)

print(Benchmark().test("MMMDCCXLIX"))
print(Benchmark().test2("MMMDCCXLIX"))
