
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        results = [""]
        for i in range(len(digits)):
            new_results = []
            for r in results:
                for letter in digits_map[digits[i]]:
                    new_results.append(r+letter)
            results = new_results
        return results
        
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))  # Output ["ad","ae","af","bd","be","bf","cd","ce","cf"]