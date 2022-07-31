from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """
        >>> Solution().leastInterval(["A","A","A","B","B","B"], 2)
        8
        >>> Solution().leastInterval(["A","A","A","B","B","B","C","C","C","D","D","D"], 2)
        12
        >>> Solution().leastInterval(["A","A","A","B","B","B","C","C","C","D","D","D"], 3)
        12
        """
        
        if n == 0:
            return len(tasks)
        
        cnt = 0
        common = Counter(tasks)
        while(tasks):
            top = common.most_common()
            i = 0
            while(top and i <= n and tasks):
                curr = top.pop(0)
                common[curr[0]] -= 1
                if(curr[1] > 0):
                    tasks.remove(curr[0])
                cnt += 1
                i+= 1
            if(i<=n and tasks):
                cnt += n - i + 1
        return cnt
    
    #-------------------------------------------------------
    #PREV SOL, NOT FAST ENOUGH
        while(tasks):
            i = 0
            top = common.most_common()
            while top:
                if(n and i == n+1):
                    break
                curr = top.pop(0)
                print(curr, top, tasks)
                i+=1
                cnt += 1
                if curr[1] == 0:
                    break
                tasks.remove(curr[0])
                common[curr[0]] -= 1
            if(n and i <= n and tasks):
                cnt += n - i + 1
        return cnt
        
        
        
            
        
        


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)