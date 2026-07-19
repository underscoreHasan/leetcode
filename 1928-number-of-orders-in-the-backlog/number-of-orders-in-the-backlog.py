import heapq
from typing import List

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buyBacklog = []   # Max heap: stored as [-price, amount]
        sellBacklog = []  # Min heap: stored as [price, amount]

        for price, amount, orderType in orders:
            # 1. If the order is a BUY order
            if orderType == 0:
                while sellBacklog and sellBacklog[0][0] <= price and amount > 0:
                    # Execute as many orders as possible at the current lowest sell price
                    execute_amount = min(amount, sellBacklog[0][1])
                    amount -= execute_amount
                    sellBacklog[0][1] -= execute_amount
                    
                    if sellBacklog[0][1] == 0:
                        heapq.heappop(sellBacklog)
                        
                # If there are remaining buy orders, add them to the backlog
                if amount > 0:
                    heapq.heappush(buyBacklog, [-price, amount])

            # 2. If the order is a SELL order
            else:
                while buyBacklog and -buyBacklog[0][0] >= price and amount > 0:
                    # Execute as many orders as possible at the current highest buy price
                    execute_amount = min(amount, buyBacklog[0][1])
                    amount -= execute_amount
                    buyBacklog[0][1] -= execute_amount
                    
                    if buyBacklog[0][1] == 0:
                        heapq.heappop(buyBacklog)
                        
                # If there are remaining sell orders, add them to the backlog
                if amount > 0:
                    heapq.heappush(sellBacklog, [price, amount])
                    
        # Sum up all remaining orders in both backlogs
        remainingBacklog = sum(amount for _, amount in buyBacklog) + sum(amount for _, amount in sellBacklog)

        return remainingBacklog % (10**9 + 7)