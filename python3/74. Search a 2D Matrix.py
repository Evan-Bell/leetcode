class Solution:
    def convert_(self, matrix,top, bottom,cols):
        ind = (top-bottom)//2 + bottom
        return matrix[int(ind//cols)][ind%cols]
    
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        >>> Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3)
        True
        >>> Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13)
        False
        >>> Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 50)
        True
        >>> Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 0)
        False
        >>> Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], -1)
        False
        >>> Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 51)
        False
        >>> Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], -2)
        False
        >>> Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], -3)
        False
        """
        j = cols = len(matrix[0])
        bottom = 0
        top = len(matrix)*j
        
        while(top-bottom):
            cur = Solution().convert_(matrix, top, bottom, cols)
            if target < cur:
                top = (top-bottom)//2 + bottom
            elif(target == cur):
                return True
            elif(top-bottom<2):
                return False
            else:
                bottom = (top-bottom)//2 + bottom
        return False
                
                
            
#         for row in matrix:
#             for item in row:
#                 if item == target:
#                     return True
                
#         return False
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)