class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         #while key in map
        numsMap = set(nums)
        res = 0
        
        starters = []
        for i in nums:
            if i-1 not in numsMap:
                length = 0
                key = i
                while key in numsMap:
                    length += 1
                    key += 1
                if length >= res:
                    res = length
            
        return res

