class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in digits:
            num *= 10
            num += i
        num += 1
        result = []
        while num != 0:
            value = num % 10
            result.insert(0, value)
            num //= 10

        return result