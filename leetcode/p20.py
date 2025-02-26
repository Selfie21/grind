class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_brack = [('{', '}'), ('(', ')'), ('[', ']')]
        stack = []
        for char in s:
            print(stack)
            if len(stack) > 0 and (stack[-1], char) in valid_brack: 
                stack.pop()
            else:
                stack.append(char)
        valid = len(stack) == 0
        return valid

s = "([])"
solution = Solution()
k = solution.isValid(s)
