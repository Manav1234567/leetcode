class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}
        val = None
        k = 0
        for i in range(len(nums)):
            if (nums[i] not in hashmap):
                nums[k] = nums[i]
                k += 1
            
            if (nums[i] == val):
                hashmap[nums[i]] = i
            else:
                val = nums[i]

        return k