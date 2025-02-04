class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                p = prices[r] - prices[l]
                maxP = max(maxP, p)
                r += 1
            else:
                l += 1
                if l >= r:
                    r+=1
        
        return maxP