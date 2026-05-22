import re

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        numfound=False
        number = 0
        need_number = False

        i = 0
        l = len(s)

        # white chars
        while i < l and s[i]==" ":
            i+=1

        if i == l:
            return number
        
        # sign
        if s[i] == "+":
            i+=1
        elif s[i] == "-":
            i+=1
            sign = -1

        while i < l and re.search('[0-9]',s[i]):
            number = number *10 + int(s[i])
            i+=1
        
        return check_limit(sign*number)

def check_limit(number):
    limit = 2**31

    if number > limit -1:
        return limit-1
    if number < -limit:
        return -limit
    return number
if __name__ == "__main__":
    solution = Solution()

    print(solution.myAtoi("      -11919730356x")) # should print -12