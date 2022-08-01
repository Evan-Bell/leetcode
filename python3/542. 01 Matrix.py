class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        """
        >>> Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
        [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        >>> Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
        [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        >>> Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
        [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        """
        
        
        #------------------------------------------
        #OK SOL, NOT THE BEST
        n,m = len(mat), len(mat[0])
        
        def neighbor(x,y):
            direc = [(1,0), (-1,0), (0,1), (0,-1)]
            res = []
            for r,c in direc:
                if x+r < n and x+r >= 0 and y+c < m and y+c >=0:
                    res.append((x+r,y+c))
            return res
        
        self.seen = set()
        
        def sum_neighbors(queue):
            while queue:
                x,y,dist = queue.pop(0)
                mat[x][y] = dist
                for r,c in neighbor(x,y):
                    if (r,c) not in self.seen:
                        queue.append((r,c, dist + 1))
                        self.seen.add((r,c))
        
        tot = []
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    tot.append((i,j,0))
                    self.seen.add((i,j))
        sum_neighbors(tot)
        return mat
        
                
        
                    
            
        

                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)