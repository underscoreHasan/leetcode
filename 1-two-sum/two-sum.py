class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = defaultdict(list)

        for i, n in enumerate(nums):
            if target-n in numsHash:
                return [i, numsHash[target-n][-1]]
            numsHash[n].append(i)
        
