class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         #while key in map
        numsSet = set(nums)
        res = 0

        for i in nums:
            if i-1 not in numsSet:
                key = i + 1
                while key in numsSet:
                    key += 1
                res = max(res, key - i)
            
        return res

