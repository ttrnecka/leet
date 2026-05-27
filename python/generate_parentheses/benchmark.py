from generate_parentheses.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, i):
        self.solution.generateParenthesis(i)

print(Benchmark().test(3))
