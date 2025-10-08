class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # if the current board value is seen in row, column or box then invalid
        ROWS, COLS = len(board), len(board[0])

        # check the row and column and the 3x3 sub-boxes
        # we can use row % 3 and col % 3 to find the corresponding box
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(ROWS):
            for c in range(COLS):
                
                if board[r][c] == '.':
                    continue

                boxIdx = (r // 3) * 3 + (c // 3) 
                # determine whether we have seen this element:
                if (board[r][c] in rows[r] or
                    board[r][c] in columns[c] or
                    board[r][c] in boxes[boxIdx]):

                    return False
                
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                boxes[boxIdx].add(board[r][c])
        
        return True
