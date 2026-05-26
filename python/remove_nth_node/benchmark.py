from .solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, i):
        self.solution.intToRoman(i)
    @benchmark(repeats=100)
    def test2(self, i):
        self.solution.intToRoman2(i)
    @benchmark(repeats=100)
    def test3(self, i):
        self.solution.intToRoman3(i)

print(Benchmark().test(3405))
print(Benchmark().test2(3405))
print(Benchmark().test3(3405))