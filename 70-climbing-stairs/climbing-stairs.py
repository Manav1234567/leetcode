class Solution:
    def __init__ (self):
        self.hmap = {}

    def climbStairs(self, n: int) -> int:
        if n in self.hmap: 
            return self.hmap[n]
        if n <= 2: 
            self.hmap[n] = n
            return n
        
        self.hmap[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.hmap[n]