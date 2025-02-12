class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        #[18,43,36,13,7]
        #[9,7,9,4,7]
        #{9:[0,2], 7:[1,4], 4:[3]}
        #[10,12,19,14]
        #[1,3,10,5]
        #{1:[0], 3:[1], 10:[2], 5:[3]}
        digitSums = defaultdict(int)
        res = -1
        
        def sumDigits(n):
            res = 0
            for d in str(n):
                res += int(d)
            return res

        for n in nums:
            k = sumDigits(n)
            if k in digitSums:
                res = max(res, n + digitSums[k])
                digitSums[k] = max(digitSums[k], n)
            else:
                digitSums[k] = n
        
        return res
            

        return res


