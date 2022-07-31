from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        >>> s = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        >>> Solution().maxAreaOfIsland(s)
        6
        """
        n = len(grid)
        m = len(grid[0])
        seen = set()
        
        
        def neighbors(x,y):
            direc = [(1,0),(-1,0), (0,1), (0,-1)]
            res = []
            for r,c in direc:
                if x+r >= 0 and x+r < n and y+c >= 0 and y+c < m:
                    res.append((x+r,y+c))
            return res
    
        
        def DFS(x,y):
            cnt = 0
            q = deque([(x,y)])
            while q:
                r,c = q.pop()
                cnt += 1
                seen.add((r,c))
                for i,j in neighbors(r,c):
                    if (i,j) not in seen and grid[i][j] == 1:
                        q.append((i,j))
                        seen.add((i,j))
            return cnt
        
        maxi = 0
        for i in range(n):
            for j in range(m):
                if (i,j) not in seen and grid[i][j] == 1:
                    maxi = max(DFS(i,j), maxi)
        return maxi
                
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)