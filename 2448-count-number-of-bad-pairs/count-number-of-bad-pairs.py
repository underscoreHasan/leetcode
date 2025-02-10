class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # good pair if j>i and j-i == nums[j] - nums[i]
        # good pair if nums[i] - i == nums[j] - j
        # difference has to be positive
        # for each pair of indices, calculate the good pair?
        #[1,3,4,5](1,3),(1,4),(1,5) => (3,4)(4,5)
        #[1,2,4,5](2,4),(2,5) => (1,2)(4,5)
        #[5,4,3,2,1] no good pairs
        #if increasing by only +1, its a good pair
        #if nums[i+1] > nums[i] by more than 1, all subsequent pairs are bad pairs

        res = 0
        #for each index, calculate the difference nums[i]-i
        #calculate how many times the same difference occurs
        diffs = defaultdict(int)

        for i in range(len(nums)):
            res += i - diffs[nums[i] - i]
            diffs[nums[i]-i] += 1
        
        return int(res)
