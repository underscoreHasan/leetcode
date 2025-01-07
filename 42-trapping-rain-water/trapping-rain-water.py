class Solution:
    def trap(self, height: List[int]) -> int:
        water = [0]*len(height)
        suffix = [0]*len(height)
        prefix = [0]*len(height)
        rightMax = leftMax = 0

        for i in range(len(height)):
            j = len(height)-1-i
            leftMax = max(leftMax, height[i])
            rightMax = max(rightMax, height[j])
            suffix[i] = leftMax
            prefix[j] = rightMax
        
        for i in range(len(height)):
            water[i] = min(prefix[i], suffix[i]) - height[i]

        return sum(water)