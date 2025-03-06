class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numSet = set()
        res = []
        for i in grid:
            for j in i:
                if j in numSet:
                    res.append(j)
                numSet.add(j)
        
        for i in range(1, (len(grid)**2)+1):
            if i not in numSet:
                res.append(i)
                break
        
        return res
