from collections import Counter

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # 0 -> 2
        # 00 -> 4
        # iterate over all binary strings, check for their existence in nums
        # n digits => 2^n strings, O(1) existence check
        n = len(nums)
        res = ""

        for i in range(n):
            res += str(int(not int(nums[i][i])))
        
        return res
            