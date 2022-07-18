class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        """
        >>> Solution().findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]])
        [1, -1, -1, -1, -1]
        """
        m = len(grid)
        n = len(grid[0])
        
        def find_path(i,j):
            if(i==m):
                return j
            if grid[i][j] == 1 :
                if j+1 >= n or grid[i][j+1] == -1:
                    return -1
                return find_path(i+1,j+1)
            if grid[i][j] == -1 :
                if j-1 < 0 or grid[i][j-1] == 1:
                    return -1
                return find_path(i+1,j-1)
            
        return [find_path(0,j) for j in range(n)]             
                
            
                

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)