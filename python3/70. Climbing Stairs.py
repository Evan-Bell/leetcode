class Solution:
    def climbStairs(self, n: int) -> int:
        vals = {0:0, 1:1, 2:2}
        for i in range(3,n+1):
            vals[i] = vals[i-1] + vals[i-2]
        return vals[n]
                
            
            
        
                
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)