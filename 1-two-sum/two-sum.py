class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2, 7, 11, 15
        numsSet = defaultdict()

        for i in range(len(nums)):
            if target-nums[i] in numsSet:
                return [i, numsSet[target-nums[i]]]
            numsSet[nums[i]] = i


            
        
