class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        map = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in range(len(s)):
            if s[i] in map:
                stack.append(s[i])
            else:
                if stack and map[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        return False if stack else True

        
