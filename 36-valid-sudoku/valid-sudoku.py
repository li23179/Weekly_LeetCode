class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        # check row
        rows_set = [set() for _ in range(9)] 
        # check col
        cols_set = [set() for _ in range(9)]
        # check block, (r, c) => (1, 1)
        blocks_set = [set() for _ in range(9)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == '.'):
                    continue
                block_index = 3 * (r // 3) + (c // 3)

                if (board[r][c] in rows_set[r] or
                    board[r][c] in cols_set[c] or
                    board[r][c] in blocks_set[block_index]):
                    return False
                
                rows_set[r].add(board[r][c])
                cols_set[c].add(board[r][c])
                blocks_set[block_index].add(board[r][c])

        return True