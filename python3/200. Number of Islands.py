class Solution:
    def get_neighbors(self, x,y,r,c):
            dir = [(1,0), (-1,0), (0,1), (0,-1)]
            res = []
            for _x,_y in dir:
                if x +_x < r and x +_x >= 0 and y + _y < c and y + _y >= 0:
                    res.append( (x+_x, y+_y) )
            return res
        
    def DFS(self, grid, x, y):
        queue = [(x,y)]
        seen = set()
        while(queue):
            (x,y) = queue.pop()
            grid[x][y] = '0'
            if((x,y) not in seen):
                for r,c in self.get_neighbors(x,y,len(grid), len(grid[0])):
                    if(grid[r][c] == '1'):
                        queue.append((r,c))
                seen.add((x,y))
        return grid
    
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    grid = self.DFS(grid, x, y)
                    cnt += 1
        return cnt
            
                
            
        
                
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)