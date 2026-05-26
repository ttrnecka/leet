
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        mapping = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in mapping:
                if len(stack) == 0:
                    return False

                if mapping[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack
        
                

if __name__ == "__main__":
    solution = Solution()

    print(solution.isValid("()")) # should print true
    print(solution.isValid("(]")) # should print false
