class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []

        for windowEnd in range(0, len(nums)):
            heapq.heappush(heap, (-nums[windowEnd], windowEnd))

            windowStart = windowEnd - k + 1
            #find the max but remove deleted elemts first
            while heap and heap[0][1] < windowStart:
                val = heapq.heappop(heap)
            
            if windowStart >= 0:
                res.append(-heap[0][0])

        return res
