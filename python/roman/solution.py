
class Solution:
    def intToRoman(self, num: int) -> str:
        numbers     = [1000 ,500    ,100    ,50     ,10 ,5      ,1  ]
        numerals    = ["M"  ,"D"    ,"C"    ,"L"    ,"X","V"    ,"I"]
        roman = ""
        while num > 0:
            num_str = str(num)
            deduct = 0
            if num_str[0] in ("4","9"):
                maxi = 0
                for i in range(len(numbers)):
                    if num >= numbers[i]:
                        maxi = i
                        break
                if num >= 400:
                    subst="C"
                    dd=100
                elif num >= 40:
                    subst="X"
                    dd=10
                else:
                    subst="I"
                    dd=1
                roman+=f"{subst}"
                roman+=f"{numerals[maxi-1]}"
                deduct = (numbers[maxi-1]-dd) 
            else:
                maxi = 0
                for i in range(len(numbers)):
                    if num >= numbers[i]:
                        maxi = i
                        break
                roman +=  f"{numerals[maxi]}"
                deduct=numbers[maxi]
            num-=deduct
        return roman
    
    def intToRoman2(self, num: int) -> str:
        # List of tuples mapping values to their Roman numeral equivalents in descending order
        roman_mapping = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        result = []
        
        for value, symbol in roman_mapping:
            if num == 0:
                break
                
            # Determine how many times the current symbol fits into num
            count = num // value
            if count > 0:
                result.append(symbol * count)
                # Reduce num by the amount we just processed
                num %= value
                
        return "".join(result)
    
    def intToRoman3(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        return (thousands[num // 1000] +
                hundreds[(num % 1000) // 100] +
                tens[(num % 100) // 10] +
                ones[num % 10])
                

if __name__ == "__main__":
    solution = Solution()

    print(solution.intToRoman(3)) # should print "III"
    print(solution.intToRoman(4)) # should print "IV"
    print(solution.intToRoman(9)) # should print "IX"
    print(solution.intToRoman(58)) # should print "LVIII"