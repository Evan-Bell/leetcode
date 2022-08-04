class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        """
        >>> Solution().letterCasePermutation("a1b2")
        ['A1B2', 'A1b2', 'a1B2', 'a1b2']
        """
        
        self.s_len = len(s)
        
        def perms(path, i):
            if i == self.s_len:
                return [path]
            if s[i] not in {'1','2','3','4','5','6','7','8','9','0'}:
                return perms(path+s[i].upper(), i+1) + perms(path+s[i].lower(), i+1)
            return perms(path+s[i], i+1)
        
        return perms('', 0)
        

        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)