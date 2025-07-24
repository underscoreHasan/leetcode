class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiralOrder = []
        while matrix:
            spiralOrder.extend(self.getBorder(matrix))
        return spiralOrder
        
    def getBorder(self, matrix: List[List[int]]) -> List[int]:
        print(matrix)
        topBorder = matrix.pop(0)
        bottomBorder = []
        if matrix:
            bottomBorder = list(reversed(matrix.pop(-1)))
        leftBorder = []
        rightBorder = []
        for row in matrix:
            if row:
                rightBorder.append(row.pop(-1))
            if row:
                leftBorder.append(row.pop(0))
        
        return topBorder + rightBorder + bottomBorder + list(reversed(leftBorder))
            

        