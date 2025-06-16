class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for i in s:
            if i in brackets:
                stack.append(i)
            elif stack and i == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []