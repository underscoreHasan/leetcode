class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        #[18,43,36,13,7]
        #[9,7,9,4,7]
        #{9:[0,2], 7:[1,4], 4:[3]}
        #[10,12,19,14]
        #[1,3,10,5]
        #{1:[0], 3:[1], 10:[2], 5:[3]}
        digitSums = defaultdict(list)
        res = -1
        
        def sumDigits(n):
            res = 0
            for d in str(n):
                res += int(d)
            return res

        for n in nums:
            k = sumDigits(n)
            heapq.heappush(digitSums[k], -n)

        for v in digitSums.values():
            if len(v) < 2:
                continue
            res = max(res, -heapq.heappop(v) + -heapq.heappop(v))

        return res