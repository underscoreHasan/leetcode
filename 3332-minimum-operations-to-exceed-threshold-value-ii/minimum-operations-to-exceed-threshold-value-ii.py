class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        def doOp(x, y):
            return min(x,y) * 2 + max(x,y)

        res = 0

        heapq.heapify(nums)

        while nums[0] < k:
            new = doOp(heapq.heappop(nums), heapq.heappop(nums))
            heapq.heappush(nums, new)
            res += 1
        
        return res

        