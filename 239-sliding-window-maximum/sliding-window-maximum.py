class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        heap = []

        #init heap
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        if heap: res.append(-heap[0][0])

        #for every startIndex in the sliding window
        for startIndex in range(1, len(nums) - k + 1):
            #add the element that just joined
            heapq.heappush(heap, (-nums[startIndex + k - 1], startIndex + k - 1))

            #find the max but remove deleted elemts first
            while heap and heap[0][1] < startIndex:
                val = heapq.heappop(heap)
            
            if heap: res.append(-heap[0][0])

        return res
