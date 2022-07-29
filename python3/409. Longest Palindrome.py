class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        >>> Solution().longestPalindrome("abccccdd")
        7
        >>> Solution().longestPalindrome("abccccdde")
        7
        """
        
        count = 0
        chars = set()
        for each in s:
            if each not in chars:
                chars.add(each)
                continue
            count += 2
            chars.remove(each)
        return count if not chars else count+1
    
        #-------------------------------------------
        #TWO LINER SOL
        o = sum([freq%2 for freq in collections.Counter(s).values()])
        return len(s) if o <= 1 else len(s)-o+1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)