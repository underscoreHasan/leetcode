import math

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        firstRow = sum(grid[0])
        secondRow = 0
        minScore = float("inf")

        for i in range(len(grid[0])):
            firstRow -= grid[0][i]
            secondScore = max(firstRow, secondRow)
            secondRow += grid[1][i]
            minScore = min(secondScore, minScore)

        return minScore