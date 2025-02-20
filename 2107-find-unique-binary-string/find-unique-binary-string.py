from collections import Counter

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # 0 -> 2
        # 00 -> 4
        # iterate over all binary strings, check for their existence in nums
        # n digits => 2^n strings, O(1) existence check
        n = len(nums)
        numsMap = Counter(nums)

        for i in range(2**n):
            if bin(i)[2:].zfill(n) not in numsMap:
                return bin(i)[2:].zfill(n)