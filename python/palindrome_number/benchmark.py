from palindrome_number.solution import Solution
from benchmark.main import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, s):
        self.solution.isPalindrome(s)
    @benchmark(repeats=100)
    def testCalc(self, s):
        self.solution.isPalindromeCalc(s)

print(Benchmark().test(100020001))
print(Benchmark().testCalc(100020001))