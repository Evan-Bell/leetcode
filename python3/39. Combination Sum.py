class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        >>> Solution().combinationSum([2,3,6,7], 7)
        [[2, 2, 3], [7]]
        """
        
        self.res = []
        
        def sum_cand(total, path, u_p):
            if total == target:
                self.res.append(path.copy())
                return
            elif total > target or not u_p:
                return
            path.append(u_p[0])
            sum_cand(total + u_p[0], path, u_p)
            path.pop()
            sum_cand(total, path, u_p[1:])
            return
        
        sum_cand(0,[], candidates.copy())
        return self.res
        
        #-----------------------------------------------
        #TOO SLOW, DOESNT WORK
        
        def convert_to_ints(p):
            out = []
            for i, val in enumerate(p):
                out += [candidates[i]]*val
            return out
                    
            
            
        def sums(total, path):
            temp = []
            for i, n in enumerate(candidates):
                if total + n <= target:
                    p = path.copy()
                    p[i] += 1
                    if total + n == target:
                        temp.append(tuple(p))
                    else:
                        temp += sums(total+n, p)

            return temp
                    
                    
        return [convert_to_ints(i) for i in set(sums(0, [0]*len(candidates)))]

        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)