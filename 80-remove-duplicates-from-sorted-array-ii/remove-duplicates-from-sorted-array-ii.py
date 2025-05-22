class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        val = None
        count = 0
        k = 0
        for i in range(len(nums)):
            if (nums[i] == val):
                count += 1
            else:
                val = nums[i]
                count = 0
                
            if count < 2:
                nums[k] = nums[i]
                k += 1

        return k