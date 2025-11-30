class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]
        empties = [] # store location that is not filled

        # two pass:
        # 1. fill all the given num in rows, cols, blocks
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                    continue
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                blocks[3*(r//3)+(c//3)].add(board[r][c])

        # 2. solve the empties position by using backtracking
        # try 1-9 on every empty position
        def dfs(index):
            # base case: if the index is out of bound
            # then we finsih solving it
            if index == len(empties):
                return True

            r, c = empties[index]
            block_index = 3 * (r//3) + (c // 3)

            for digit in "123456789":    
                # check row, col, block
                if digit not in rows[r] and digit not in cols[c] and digit not in blocks[block_index]:
                    # try the current digit
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    blocks[block_index].add(digit)
                    
                    # if the recursive cases works then this num is fine
                    if dfs(index+1):
                        return True

                    board[r][c] = '.'
                    rows[r].discard(digit)
                    cols[c].discard(digit)
                    blocks[block_index].discard(digit)
            
            return False

        dfs(0)