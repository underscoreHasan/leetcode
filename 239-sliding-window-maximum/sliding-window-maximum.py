class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for windowEnd in range(len(nums)):
            windowStart = windowEnd - k + 1
            
            while q and nums[q[-1]] <= nums[windowEnd]:
                q.pop()

            q.append(windowEnd)

            while q and q[0] < windowStart:
                q.popleft()

            if windowStart >= 0:
                res.append(nums[q[0]])

        return res