class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = nums[0] % 2
        for i in nums[1:]:
            if (parity ^ i % 2) != 1:
                return False
            parity = i % 2
        
        return True
        