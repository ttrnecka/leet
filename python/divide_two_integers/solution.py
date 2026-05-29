
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        
        negative = (dividend<0) != (divisor<0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            mult = 1
            value = divisor
            while value+value <= dividend:
                value+=value
                mult+=mult
            
            dividend-=value
            result+=mult

        if negative:
            result = ~result +1

        if result < -2**31:
            return -2**31
        elif result >= 2**31:
            return 2**31
        else:
            return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.divide(10, 3)) # should print 3
    print(solution.divide(7, -3)) # should print -2