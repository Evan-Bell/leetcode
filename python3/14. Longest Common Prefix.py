class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        >>> Solution().longestCommonPrefix(["flower","flow","flight"])
        'fl'
        >>> Solution().longestCommonPrefix(["dog","racecar","car"])
        ''
        """
        
        res = ""
        m1, m2 = max(strs), min(strs)
        for i, ch in enumerate(m2):
            if(ch != m1[i]):
                break
            res += ch
        return res
                
        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)