class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        >>> Solution().longestPalindrome("abccccdd")
        7
        >>> Solution().longestPalindrome("abccccdde")
        7
        """
        count = 0
        single_added = False
        for each in set(s):
            appears = s.count(each)
            if(not single_added and appears%2==1):
                count += appears
                single_added = True
            else:
                count += s.count(each)-s.count(each)%2
        return int(count)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)