from divide_two_integers.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, dividend, divisor):
        self.solution.divide(dividend, divisor)

print(Benchmark().test(1000, 3))
print(Benchmark().test(2147483647, 1))
