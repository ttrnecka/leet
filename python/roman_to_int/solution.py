
class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        result = 0
        for i in range(len(s)):
            if i+1 < len(s) and map[s[i]] < map[s[i+1]]:
                result-=map[s[i]]
            else:
                result+=map[s[i]]
        return result
    # about ~20% faster but uses 20% more memory
    def romanToInt2(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
                

if __name__ == "__main__":
    solution = Solution()

    print(solution.romanToInt("III")) # should print 3
    print(solution.romanToInt("IV")) # should print 4
    print(solution.romanToInt("IX")) # should print 9
    print(solution.romanToInt("LVIII")) # should print 58