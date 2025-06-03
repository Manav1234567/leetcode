class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1]
        index = 0
        for i in s:
            if i == ' ':
                index += 1
            else:
                break

        count = 0
        for i in range(index, len(s)):
            if s[i] != ' ':
                count += 1
            else:
                break

        return count
