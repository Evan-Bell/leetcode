class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """
        >>> Solution().insert([[1,3],[6,9]], [2,5])
        [[1, 5], [6, 9]]
        >>> Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
        [[1, 2], [3, 10], [12, 16]]
        >>> Solution().insert([[1,5]], [2,3])
        [[1, 5]]
        >>> Solution().insert([[1,5]], [2,6])
        [[1, 6]]
        """
        
        
        res = []
        i = -1
        I = newInterval
        
        for i, [s,e] in enumerate(intervals):
            if e < I[0]:
                res.append([s,e])
            elif s > I[1]:
                i -= 1
                break
            else:
                I = [min(I[0],s), max(I[1],e)]
        
        return res + [I] + intervals[i+1:]
                
        
        #--------------------------------
        #SOL WORKS, BUT UGLY CODE
        I = newInterval
        res = []
        I_added = False
        
        if not intervals:
            return [I]
        if I[0] > intervals[-1][1]:
            return intervals + [I]
        if I[1] < intervals[0][0]:
            return [I] + intervals 
        
        for i, [s,e] in enumerate(intervals):
            if e < I[0]:
                res.append([s,e])
            elif s > I[1]:
                if not I_added:
                    res.append(I)
                    I_added = True
                res.append([s,e])
            else:
                if not I_added:
                    res.append(I)
                    I_added = True
                I = [min(I[0],s), max(I[1],e)]
                res[-1] = I
        return res
                
        
        #------------------------------------
        #STILL SLOPPY, DOESN'T WORK
        s, e = newInterval
        left = [i for i in intervals if i[0]<=s]
        right = [i for i in intervals if i[1]>=e]
        
        l, r = False, False
        
        if not left and not right:
            return [newInterval]
        
        if s > left[-1][1]:
            l = True
        if e < right[0][0]:
            r = True
            
        if l and r:
            return left + [[s,e]] + right
        if l and not r:
            right[0][0] = s
            return left + right
        if r and not l:
            left[-1][1] = e
            return left + right
        
        return left[:-1] + [[left[-1][0],right[0][1]]] + right[1:]
        
        #----------------------------------------
        #SLOPPY, DOESNT WORK
        res = []
        start, stop = newInterval
        begin, end = None, None
        ind = None
        for i,interval in enumerate(intervals):
            print(i, interval, ind, begin, end)
            if ind == None:
                if start >= interval[0]:
                    if start <= interval[1]:
                        begin = interval[0]
                        ind = i
                    else:
                        res += [interval]
                        continue
                elif start < interval[0]:
                    begin = start
                    ind = i
                    
            
            if stop >= interval[0]:
                if stop <= interval[1]:
                    end = interval[1]
                    res += intervals[i:]
                    break
                else:
                    end = stop
                    res += intervals[i:]
                    break
            else:
                end = stop
                res += intervals[i-1:]
                break     
                
        if ind == None:
            res += [newInterval]
        elif end == None:
            res[-1] = newInterval[1]
        else:  
            res[ind] = [begin,end]
        return res
            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)