class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        best = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                stack = []
                score = 0
                visited = [[False for _ in range(len(grid[i]))] for _ in range(len(grid))]
                stack.append([i,j])
                while stack:
                    r, c = stack.pop()
                    if r >= len(grid) or r < 0 or c>=len(grid[r]) or c<0:
                        continue
                    if grid[r][c] == 0:
                        continue
                    if visited[r][c] == True:
                        continue
                    score += grid[r][c]
                    visited[r][c] = True
                    best = max(best, score)
                    stack.append([r, c + 1])
                    stack.append([r, c - 1])
                    stack.append([r + 1, c])
                    stack.append([r - 1, c])
        
        return best