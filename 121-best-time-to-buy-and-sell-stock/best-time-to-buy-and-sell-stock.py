class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = [0]*len(prices)
        minBuy = prices[0]

        for i, sell in enumerate(prices):
            maxP[i] = sell - minBuy
            minBuy = min(minBuy, sell)

        return max(maxP)
