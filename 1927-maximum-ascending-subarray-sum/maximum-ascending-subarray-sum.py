class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l, r = 0, 1
        res = 0
        curr = nums[0]

        while r < len(nums):
            if nums[r] > nums[r-1]:
                curr += nums[r]
                r += 1
            else:
                res = max(res, curr)
                l = r
                r += 1
                curr = nums[l]
        
        return max(res, curr)
