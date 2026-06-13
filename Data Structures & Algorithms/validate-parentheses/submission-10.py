class Solution:
    def isValid(self, s: str) -> bool:
        openClose = {'(':')','[':']', '{':'}'}
        stack = []
        for i in s:
            if i in openClose:
                stack.append(i)
            else:
                if stack and openClose[stack[-1]] != i:
                    return False
                elif stack:
                    stack.pop()
                else:
                    return False
        return True if not stack else False