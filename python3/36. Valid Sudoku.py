class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        >>> Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
        True
        >>> Solution().isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
        False

        """
        col_seen = {0:set(),
                   1:set(),
                    2:set(),
                   3:set(),
                   4:set(),
                   5:set(),
                   6:set(),
                   7:set(),
                   8:set()}
        
        block_seen = {0:set(),
                   1:set(),
                    2:set(),
                   3:set(),
                   4:set(),
                   5:set(),
                   6:set(),
                   7:set(),
                   8:set()}
        
        
        for i in range(9):
            row_seen = set()
            for j in range(9):
                item = board[i][j]
                if(item != "."):
                    if(item in row_seen or item in col_seen[j] or item in block_seen[3*(i//3)+j//3]):
                        return False
                    row_seen.add(item)
                    col_seen[j].add(item)
                    block_seen[3*(i//3)+j//3].add(item)
                
        return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)