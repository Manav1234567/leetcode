class Solution:
    def isValid(self, s: str) -> bool:
        opening = {"(": 1, "{": 2, "[": 3}
        closing = {")": 1, "}": 2, "]": 3}
        valid = True
        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            elif stack != [] and opening[stack[-1]] == closing[i]:
                stack.pop()
            else:
                return False
        return stack == []