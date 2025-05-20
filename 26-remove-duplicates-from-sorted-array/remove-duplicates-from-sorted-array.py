class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}

        k = 0
        for i in range(len(nums)):
            if (nums[i] not in hashmap):
                nums[k] = nums[i]
                k += 1

            hashmap[nums[i]] = i

        return k