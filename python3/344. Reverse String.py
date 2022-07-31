class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        >>> s = ["h","e","l","l","o"]
        >>> Solution().reverseString(s)
        >>> s==["o","l","l","e","h"]
        True
        """
        s_len = len(s)
        for i in range(s_len-s_len//2):
            temp = s[i]
            s[i] = s[s_len-i-1]
            s[s_len-i-1] = temp
        
        
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)