class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for windowEnd in range(len(nums)):
            windowStart = windowEnd - k + 1
            # 1. Maintain the decreasing order property
            # Remove elements from the back that are smaller than the current element
            while q and nums[q[-1]] <= nums[windowEnd]:
                q.pop()

            # Add the current index to the back
            q.append(windowEnd)

            # 2. repeatedly remove the front element if it's out of window bounds
            while q and q[0] < windowStart:
                q.popleft()

            # 3. Append the maximum element to our results
            if windowStart >= 0:
                res.append(nums[q[0]])

        return res