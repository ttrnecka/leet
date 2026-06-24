class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        result = [0] * (len(num1)+len(num2))

        n1 = num1.encode()
        n2 = num2.encode()
        zero = "0".encode()[0]

        for i in range(len(n1)-1,-1,-1):
            v1 = n1[i] - zero
            for j in range(len(n2)-1,-1,-1):
                v2 = n2[j] - zero

                result[i+j+1] += (v1 * v2)
                if result[i+j+1] >= 10:
                    result[i+j] += result[i+j+1] // 10 
                    result[i+j+1] = result[i+j+1] % 10

        if result[0] == 0:
            result = result[1:]

        for i in range(len(result)):
            result[i] = str(result[i])

        return f"{''.join(result)}"
if __name__ == "__main__":
    solution = Solution()

    print(solution.multiply("2", "3")) # should print "6"
    print(solution.multiply("123", "456")) # should print "56088"