from phone_letters.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, number):
        self.solution.letterCombinations(number)

print(Benchmark().test("23"))