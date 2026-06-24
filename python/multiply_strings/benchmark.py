from multiply_strings.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, num1, num2):
        self.solution.multiply(num1, num2)

print(Benchmark().test("2", "3"))