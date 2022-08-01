class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        >>> Solution().merge([[1,3],[6,9]])
        [[1, 3], [6, 9]]
        >>> Solution().merge([[1,3],[6,9],[2,6],[8,10]])
        [[1, 10]]
        >>> Solution().merge([[1,3],[6,9],[2,6],[8,10],[12,16]])
        [[1, 10], [12, 16]]
        >>> Solution().merge([[1,5]])
        [[1, 5]]
        """
        
        
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key = lambda x: x[0])
        res = [intervals.pop(0)]
        for n in intervals:
            if n[0] <= res[-1][1]:
                res[-1][1] = max(n[1], res[-1][1])
            else:
                res.append(n)
        return res
        
        
        #---------------------------------------
        #SOL DOES NOT WORK, SLOPPY
        inters = {}
        for s,e in sorted(intervals, key = lambda x: x[0]):
            if s not in inters:
                inters[s] = 0
            inters[s] = max(inters[s], e)
        
        seen = set()
        res = []
        
        for key, val in inters.items():
            if(key not in seen):
                end = val
                for i in range(key, val+1):
                    if i in inters and inters[i] >= end:
                        end = inters[i]
                    seen.add(i)
                res += [[key, end]]
        return res
            
            
        
        
        #------------------------------
        #REALLY POOR SOL, DOES NOT WORK
        nums  = set()
        for i in intervals:
            [nums.add(g) for g in range(i[0], i[1])]
            if i[0] == i[1]:
                nums.add(i[0])
            
        last = i = min(nums)
        nums.remove(i)
        res = [[i]]
        while(nums):
            i = min(nums)
            nums.remove(i)
            if i != last + 1:
                res[-1].append(last+1)
                res.append([i])
            last = i
        res[-1].append(i+1)
        return res
            
        
            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)