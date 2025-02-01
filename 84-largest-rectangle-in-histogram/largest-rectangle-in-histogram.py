class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        lBoundary = [-1]*n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                lBoundary[i] = stack[-1]
            stack.append(i)

        print(lBoundary)

        rBoundary = [n]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rBoundary[i] = stack[-1]
            stack.append(i)

        print(rBoundary)

        bestArea = float("-inf")

        for i in range(n):
            currArea = heights[i] * (1+rBoundary[i]-1 - (lBoundary[i]+1))
            bestArea = max(bestArea, currArea)

        return bestArea

        #[-1, -1, 1, 1, 1, 4]
        #[1, 6, 3, 6, 6, 6]

        #>
        #[-1, -1, 1, 1, 3, 4]
        #[1, 6, 3, 4, 6, 6]


