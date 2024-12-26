class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         #while key in map
        numsMap = {}
        res = 0

        for i in nums:
            numsMap[i] = None
        
        starters = []
        for i in nums:
            if i-1 not in numsMap:
                starters.append(i)

        for i in starters:
            length = 0
            key = i
            while key in numsMap:
                length += 1
                key += 1
            if length >= res:
                res = length
        
        return res

