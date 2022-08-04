class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        """
        >>> Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
        5
        """
        self.seen = set()
        
        def BFS():
            q = [stones[0]]
            cnt = 0
            while q:
                curr = q.pop(0)
                stones.remove(curr)
                for x,y in stones:
                    if (x == curr[0] or y == curr[1]) and (x,y) not in self.seen:
                        q.append([x,y])
                        self.seen.add((x,y))
                        cnt += 1
            return cnt
        
        total = 0
        while(stones):
            total += BFS()
        return total 
    
        #---------------------------------------------------
        #REALLY LONG SOL, NOT GREAT FOR JUST FINDING NUMBER, DOESNT WORK BUT COULD BE GOOD FOR FINDING ACTUAL PATH
        rows = defaultdict(int)
        cols = defaultdict(int)
        vals = {}
        for x,y in stones:
            rows[x] += 1
            cols[y] += 1
            vals[(x,y)] = 0
        for x,y in stones:
            if rows[x]+cols[y]-2 > 0:
                vals[(x,y)] = rows[x]+cols[y]-2
        
        def print_grid():
            n = max(max(rows), max(cols))
            print('\n')
            for i in range(n+1+2):
                tot = ''
                for j in range(n+1+2):
                    if (i,j) in vals:
                        tot += 'X|'
                    else:
                        tot += ' |'
                print(tot)
            print('\n')
            
            
        def remove_neighbors(x,y):
            rows[x] -=1 
            cols[y] -= 1
            for x,y in stones:
                vals[(x,y)] = rows[x]+cols[y]-2
        
        cnt = 0
        while vals:
            min_coor = min(vals, key=vals.get)
            min_val = vals[min_coor]
    
            print(min_coor,min_val)
            print_grid()
            if min_val == 0:
                stones.remove([*min_coor])
                del vals[min_coor]
                continue
            cnt += 1
            stones.remove([*min_coor])
            del vals[min_coor]
            remove_neighbors(*min_coor)
            
        return cnt
        
        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)