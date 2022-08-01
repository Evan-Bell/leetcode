class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        >>> Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
        4
        >>> Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
        -1
        >>> Solution().orangesRotting([[0,2]])
        0"""
        
        #THIS IS VERY FAST
        m,n = len(grid), len(grid[0])
        rotten, fresh = [], 0
        minutes = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rotten += [(i,j)]
        
        while rotten:
            minutes += 1
            for _ in range(len(rotten)):
                x,y = rotten.pop(0)
                for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    if 0<=dx+x<m and 0<=dy+y<n and grid[x+dx][y+dy] == 1:
                        fresh -= 1
                        rotten.append((x+dx, y+dy))
                        grid[x+dx][y+dy] = 2
                        
        return -1 if fresh != 0 else max(minutes-1, 0)
        
        
        #----------------------------------------------------
        #SOL WORKS BUT A BIT MESSY
        
        m = len(grid)
        n = len(grid[0])
        
        visited = set() 
        
        def neighbors(x,y):
            res = []
            direc = [(1,0), (-1,0), (0,1), (0,-1)]
            for r,c in direc:
                if x+r >= 0 and x+r < m and y+c >= 0 and y+c < n and (x+r, y+c) not in visited:
                    res += [(x+r, y+c)]
            return res
        
        def BFS(grid, queue):
            temp = []
            if not queue:
                return -1
            while(queue):
                curr = queue.pop(0)
                if curr not in visited:
                    for x,y in neighbors(*curr):
                        if(grid[x][y] == 1):
                            temp += [(x,y)]
                            grid[x][y] = 2
                    visited.add(curr)
            return 1 + BFS(grid, temp)
        
        
        rotten = []
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 2):
                    rotten.append((i,j))
                    
        if not rotten and not [i for i in grid if 1 in i]:
            return 0
        
        c = BFS(grid, rotten)
        print(grid, c)
        if not [i for i in grid if 1 in i]:
            return c
        return -1
                    
            
        

                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)