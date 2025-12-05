class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        [1, 4, 7].   [7, 4, 1]
        [2, 5, 8] => [8, 5, 2]
        [3, 6, 9].   [9, 6, 3]
        """
        
        # transpose
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            for c in range(r, COLS):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # reverse
        for r in range(ROWS):
            for c in range(COLS//2):
                matrix[r][c], matrix[r][COLS - c - 1] = matrix[r][COLS - c - 1], matrix[r][c]
                