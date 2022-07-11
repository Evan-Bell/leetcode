class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        >>> Solution().isSubsequence("abc", "ahbgdc")
        True
        >>> Solution().isSubsequence("axc", "ahbgdc")
        False
        >>> Solution().isSubsequence("", "ahbgdc")
        True
        """

        temp = s+""
        for char in list(t):
            if(not temp):
                return True
            if(char == temp[0]):
                temp = temp[1:]
        return not temp

        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)