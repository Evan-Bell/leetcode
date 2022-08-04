class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        >>> Solution().combine(4, 2)
        [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        >>> Solution().combine(2, 1)
        [[1], [2]]
        """
        
        def combs(path, start):
            if len(path) == k:
                return [path]
            out = []
            for i in range(start,n+1):
                out += combs(path+[i], i+1)
            return out
        
        return combs([], 1)
        

        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)