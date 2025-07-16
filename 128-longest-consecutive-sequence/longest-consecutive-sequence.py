class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 100, 4, 200, 1, 3, 2 -> 1,2,3,4
        # sort the array
        # count the longest sequence O(n+nlogn)
        """
        make a set of all numbers in the array
        res = 0
        len = 0
        for each n in set
            len+=1
            if n-1 not in set
                compare lengths
                set len to 0
            if n-1 in set
                continue
        """
        numsSet = set(nums)
        res = 0

        for n in numsSet: 
            if n - 1 not in numsSet: #start of a sequence
                len = 0
                curr = n #the current candidate number we want to check
                while curr in numsSet: #keep counting until the sequence breaks
                    curr += 1
                    len += 1
                res = max(len,res)

        return res
