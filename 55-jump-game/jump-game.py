class Solution:
    def canJump(self, nums: List[int]) -> bool:
        skip = 0
        for i in nums:
            if skip < 0:
                return False
            elif i > skip:
                skip = i
            skip -= 1

        return True