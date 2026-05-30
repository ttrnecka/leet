from substring_with_concatenation_of_all_words.solution import Solution
from benchmark import benchmark


class Benchmark:
    def __init__(self):
        self.solution = Solution()
    @benchmark(repeats=100)
    def test(self, s, words):
        self.solution.findSubstring(s, words)

print(Benchmark().test("barfoothefoobarman", ["foo", "bar"]))
print(Benchmark().test("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))