class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        >>> Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
        [[4, 0], [0, 4], [3, 1], [1, 4], [3, 0], [2, 2], [1, 3]]
        """
        n = len(heights)
        m = len(heights[0])
        self.pacific = set()
        self.atlantic = set()
        
        #@cache
        def neighbors(x,y):
            res = []
            direc = [(1,0), (-1,0), (0,1), (0,-1)]
            for r,c in direc:
                if x+r >= 0 and x+r < n and y+c >= 0 and y+c < m:
                    res.append((x+r,y+c))
            return res
                
        
        def check_path(x,y, path):
            path.add((x,y))
            for r,c in neighbors(x,y):
                if(heights[x][y] <= heights[r][c]):
                    if((r,c) not in path):
                        path.add((r,c))
                        check_path(r,c, path)       
            return
            
        
        for i in range(n):
            check_path(i,0, self.pacific)
            check_path(i,m-1, self.atlantic)
        visited = set()
        for j in range(m):
            check_path(0,j, self.pacific)
            check_path(n-1, j, self.atlantic)
        return [[x,y] for (x,y) in list(self.atlantic & self.pacific)]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)