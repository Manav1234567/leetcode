class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        profit = 0
        for i in prices:
            if i > prev:
                profit += i - prev
            prev = i
        return profit