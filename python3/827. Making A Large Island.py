from collections import defaultdict

class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        """
        >>> Solution().largestIsland([[1,0],[0,1]])
        3
        >>> Solution().largestIsland([[1,1],[1,0]])
        4"""
        
        seen = set()
        n = len(grid)
        borders = defaultdict(int)
        
        def neighbors(x,y):
            res = []
            direc = [(1,0),(-1,0),(0,1),(0,-1)]
            for i,j in direc:
                if not ((x+i < 0 or x+i >= n) or (y+j < 0 or y+j >= n)):
                    res.append( (x+i, y+j) )
            return res
                    
        def BFS(grid, r,c):
            queue = [(r,c)]
            res = 0
            temp_borders = set()
            visited = set()
            while queue:
                x,y = queue.pop()
                if((x,y) not in visited):
                    if(grid[x][y] == 1):
                        res += 1
                        queue += neighbors(x,y)
                        visited.add((x,y))
                    else:
                        temp_borders.add((x,y))
                    seen.add((x,y))
            
            
            for b in temp_borders:
                borders[b] += res
            return res
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in seen:
                    BFS(grid, i, j)
        
        if not borders:
            if [i for i in grid if 1 in i]:
                return len(grid)**2
            return 1
        
        largest = 0
        for val in borders.values():
            largest = max(largest, val+1)
        return largest
    
        
        #-----------------------------------------------------
        #ATTEMPT TOO SLOW
        seen = set()
        n = len(grid)
        
        def neighbors(x,y):
            res = []
            direc = [(1,0),(-1,0),(0,1),(0,-1)]
            for i,j in direc:
                if not ((x+i < 0 or x+i >= n) or (y+j < 0 or y+j >= n)):
                    res.append( (x+i, y+j) )
            return res
                    
        def BFS(grid, r,c):
            queue = [(r,c)]
            borders = []
            res = 0
            visited = set()
            while queue:
                x,y = queue.pop()
                if((x,y) not in visited):
                    if(grid[x][y] == 1):
                        res += 1
                        queue += neighbors(x,y)
                        visited.add((x,y))
                    else:
                        borders.append((x,y))
                    seen.add((x,y))
            return res,borders
        
        
        
        largest,borders = BFS(grid, 0, 0)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0 and (i,j) not in seen:
                    grid[i][j] = 1
                    largest = max(largest, BFS(grid, i, j))
                    grid[i][j] = 0
        return largest
            
                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)