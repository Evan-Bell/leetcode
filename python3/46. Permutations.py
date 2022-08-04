class Solution:
    def permute(self, nums: list[int]) ->list[list[int]]:
        """
        >>> Solution().permute([1,2,3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        """
        def perm(inp, path):
            if not inp:
                return [path]
            out = []
            s = set(inp)
            for i in range(len(inp)):
                s.remove(inp[i])
                out += perm(list(s),path+[inp[i]])
                s.add(inp[i])
            return out
                
        return perm(nums, [])
            
        
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)