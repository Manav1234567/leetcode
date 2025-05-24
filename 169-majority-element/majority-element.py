class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = majority = 0
        
        for n in nums:
            if majority == 0:
                res = n
            
            majority += 1 if n == res else -1
        
        return res

        # For Boyer Moore Voting algorithm, 
        # if you are not given that the majority
        # element occurs more than n/2 times,
        # you need to check for it separately.