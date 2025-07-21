class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        numMagicSquares = 0

        numRows = len(grid)
        numCols = len(grid[0])

        for i in range(numRows - 2):
            for j in range(numCols - 2):
                # print(i,j)
                if self.checkForMagicSquare(grid, i, j):
                    numMagicSquares += 1

        return numMagicSquares

    def checkForMagicSquare(self, grid, i, j):
        """
        there are 4 conditions:
        1) numbers from 1-9
        2) 3 rows each one sum is equal
        3) 3 cols each one sum is equal
        4) 2 diagnols equal sum
        """
        submatrix = [row[j : j + 3] for row in grid[i : i + 3]]

        # 1 
        submatrixNums = {elem for row in submatrix for elem in row}
        cond1 = submatrixNums == set(range(1,10))

        # 2
        cond2 = sum(submatrix[0]) == sum(submatrix[1]) == sum(submatrix[2])

        # 3
        transpose = list(zip(*submatrix))
        cond3 = sum(transpose[0]) == sum(transpose[1]) == sum(transpose[2])

        # 4
        leadingDiag = 0
        antiDiag = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if i == j:
                    leadingDiag += submatrix[i][j]
                if j == 2 - i:
                    antiDiag += submatrix[i][j]

        cond4 = leadingDiag == antiDiag

        return cond1 and cond2 and cond3 and cond4
