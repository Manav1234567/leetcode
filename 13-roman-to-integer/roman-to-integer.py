class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        count = 0
        for i in range(len(s)):
            if i+1 < len(s) and sym[s[i+1]] > sym[s[i]]:
                count -= sym[s[i]]
            else:
                count += sym[s[i]]
        return count