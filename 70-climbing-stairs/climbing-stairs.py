class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        n_2 = 2
        n_1 = 1

        for i in range(3, n + 1):
            temp = n_2 + n_1
            n_1 = n_2
            n_2 = temp
        
        return n_2
