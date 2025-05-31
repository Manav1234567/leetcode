class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            pos = t.find(i)
            if pos < 0:
                return False
            t = t[pos+1:]
            print(t)
        return True

        