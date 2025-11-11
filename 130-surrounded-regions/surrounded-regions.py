class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # capture a surrounded region => 
        # capture everything expect the unsurrounded region
        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != 'O'):
                return

            board[r][c] = 'T'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        ROWS, COLS = len(board), len(board[0])

        # mark the outer region 'O' as 'T'
        # we don't change since it is on the bound of the board
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS-1] or
                    c in [0, COLS-1] and
                    board[r][c] == 'O'):

                    dfs(r,c)

        # change all the 'O's into 'X'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        # change all the 'T's back to 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

                
        