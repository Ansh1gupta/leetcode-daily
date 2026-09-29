class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        r = len(matrix[0])

        row = [0] * l
        col = [0] * r

        for i in range(l):
            for j in range(r):
                if matrix[i][j] == 0:
                    row[i] = -1
                    col[j] = -1

        for i in range(l):
            for j in range(r):
                if row[i] == -1 or col[j] == -1:
                    matrix[i][j] = 0