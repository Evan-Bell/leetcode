class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        res = [[1]*n for i in range(m)]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                res[i][j] = res[i+1][j] + res[i][j+1]
        return res[0][0]
    
        #RECURSIVE VERSION
        def DFS(x,y, seen = set()):
            if x >= m or y >= n:
                return 0
            if (x,y) == (m-1, n-1):
                return 1
            if ((x,y) not in seen):
                seen.add((x,y))
            return DFS(x+1,y, seen) + DFS(x,y+1, seen)
            
        return DFS(0,0)
  
            
        
                
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)