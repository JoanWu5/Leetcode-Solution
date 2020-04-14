class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def is_unit_valid(unit):
            unit = [i for i in unit if i!='.']
            return len(set(unit)) == len(unit)

        def is_row_valid(board):
            for row in board:
                if not is_unit_valid(row):
                    return False
            return True

        def is_col_valid(board):
            for col in zip(*board):
                if not is_unit_valid(col):
                    return False
            return True
        
        def is_square_valid(board):
            for i in (0,3,6):
                for j in (0,3,6):
                    square = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                    if not is_unit_valid(square):
                        return False
            return True

        return is_row_valid(board) and is_col_valid(board) and is_square_valid(board)

s = Solution()
print(s.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))