class Solution:
    def __init__ (self):
        self.hmap = {}

    def climbStairs(self, n: int) -> int:
        if n in self.hmap: 
            return self.hmap[n]
        elif n <= 2: 
            self.hmap[n] = n
            return n
        
        left = self.hmap[n-1] if n-1 in self.hmap else self.climbStairs(n - 1)
        right = self.hmap[n-2] if n-2 in self.hmap else self.climbStairs(n - 2)
        self.hmap[n] = left + right

        return  self.hmap[n]