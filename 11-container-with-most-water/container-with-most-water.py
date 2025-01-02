class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0

        l, r = 0, len(height) - 1

        while l < r:
            candidate = min(height[l], height[r]) * (r - l)
            if candidate > best:
                best = candidate
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best
