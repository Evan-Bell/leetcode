class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        >>> Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
        >>> Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        """
        low_row = low_col = 0
        high_row = len(matrix)
        high_col = len(matrix[0])
        res = []
        while(len(res) < len(matrix)*len(matrix[0])):
            
            for i in range(high_col-low_col):
                res.append((low_row,low_col+i))
            low_row += 1
            
            for i in range(high_row-low_row):
                res.append((low_row+i,high_col-1))
            high_col -= 1
            
            for i in range(high_col-low_col):
                res.append((high_row-1,high_col-i-1))
            high_row -= 1
            
            for i in range(high_row-low_row):
                res.append((high_row-i-1,low_col))
            low_col += 1
            
        return [matrix[i][j] for i,j in res[:len(matrix)*len(matrix[0])]]

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)