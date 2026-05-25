class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True

    def isPalindromeCalc(self, x: int) -> bool:
        reversed_num = 0
        n = x
        while n > 0:
            reversed_num = reversed_num * 10 + (n % 10)
            n = n // 10

        if reversed_num == x:
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(1111)) # should print true
    print(solution.isPalindrome(1211)) # should print false