class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        >>> Solution().minimumTotal([[2],[3,4],[1,5,6]])
        6
        >>> Solution().minimumTotal([[-1],[-3, 100]])
        -4
        """

        for r in range(len(triangle)-2, -1, -1):
            for i in range(r+1):
                triangle[r][i] += min(triangle[r+1][i], triangle[r+1][i+1])
        return triangle[0][0]
        
        
    #--------------------------------------------
    #OK SOL BUT TOO SLOW
        self.max_lev = len(triangle)
        self.min = float('inf')
        
        def min_path(total = 0, i = 0, level = 0):
            if level == self.max_lev:
                return total
            l = min_path(total+triangle[level][i], i, level+1)
            r = min_path(total+triangle[level][i], i+1, level+1)
            self.min =  min(l,r)
            return self.min
        
        return min_path()
            
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)