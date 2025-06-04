class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in strs:
            for j in range(len(prefix)):
                if j < len(i) and prefix[j] != i[j]:
                    prefix = prefix[:j]
                    break
                elif j >= len(i):
                    prefix = prefix[:len(i)]

        return prefix