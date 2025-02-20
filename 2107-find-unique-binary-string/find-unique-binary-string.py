from collections import Counter

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        numsMap = Counter(nums)

        for i in range(2 ** n):
            binary_str = bin(i)[2:].zfill(n)  # Convert to binary and pad with leading zeros
            if binary_str not in numsMap:
                return binary_str