class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {nums[i]: 0 for i in range(len(nums))}

        for i in range(len(nums)):
            hashmap[nums[i]] += 1

        print(hashmap)
        return max(hashmap, key = hashmap.get)