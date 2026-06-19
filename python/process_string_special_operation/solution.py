class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for char in s:
            if char == '*':
                if len(result) > 0:
                    result = result[0:len(result)-1]
            elif char =='#':
                result +=result
            elif char =='%':
                result = result[::-1]
            else:
                result += char

        return result