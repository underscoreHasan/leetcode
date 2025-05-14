class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = {}

        for i, n in enumerate(nums):
            if target-n in numsHash:
                return [i, numsHash[target-n]]
            numsHash[n]=i
        
