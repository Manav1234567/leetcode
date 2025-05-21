class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}
        val = None
        count = 0
        k = 0
        for i in range(len(nums)):
            if (nums[i] not in hashmap):
                nums[k] = nums[i]
                k += 1
            
            if (nums[i] == val):
                count += 1
                if count >= 1:
                    hashmap[nums[i]] = i
            else:
                val = nums[i]
                count = 0


        return k