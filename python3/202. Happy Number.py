class Solution:
    def isHappy(self, n: int) -> bool:
        """
        >>> Solution().isHappy(19)
        True
        >>> Solution().isHappy(2)
        False
        """
        
        seen = set()
        while(n>1):
            s = 0
            while(n>0):
                s += (n%10)**2
                n = n//10
            n=s
            if(n in seen):
                return False
            seen.add(n)
        return True
            

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)