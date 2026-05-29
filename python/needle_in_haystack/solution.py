
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack)-len(needle)+1):
            match = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    match = False
                    break
            if match:
                return i

        return -1


if __name__ == "__main__":
    solution = Solution()

    print(solution.strStr("sadbutsad", "sad")) # should print 0
    print(solution.strStr("leetcode", "leeto")) # should print -1