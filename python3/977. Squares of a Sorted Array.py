class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """
        >>> Solution().sortedSquares([-4,-1,0,3,10])
        [0, 1, 9, 16, 100]
        """
        
        
        
        #ONE LINE
        return sorted([i**2 for i in nums])

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)