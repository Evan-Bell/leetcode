class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def get_neighbors(x,y,r,c):
            dir = [(1,0), (-1,0), (0,1), (0,-1)]
            res = []
            for _x,_y in dir:
                if x +_x < r and x +_x >= 0 and y + _y < c and y + _y >= 0:
                    res.append( (x+_x, y+_y) )
            return res
        
        orig = image[sr][sc]
        if(orig == color):
            return image
        rows = len(image)
        cols = len(image[0])
        queue = [(sr,sc)]
        seen = set()
        while(queue):
            (x,y) = queue.pop()
            if (x,y) not in seen and image[x][y] == orig:
                image[x][y] = color
                for r,c in get_neighbors(x,y, rows, cols):
                    queue.append((r,c))
                seen.add((x,y))
        return image
            
        
                
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)