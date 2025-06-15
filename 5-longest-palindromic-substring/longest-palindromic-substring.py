class Solution:
    def longestPalindrome(self, s: str) -> str:
        palin = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp = s[i:j+1]
                if len(temp) > len(palin) and temp == temp[::-1]:
                    palin = temp

        return palin