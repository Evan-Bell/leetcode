class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        >>> Solution().lengthOfLongestSubstring("abcabcbb")
        3
        >>> Solution().lengthOfLongestSubstring("bbbbb")
        1
        >>> Solution().lengthOfLongestSubstring("pwwkew")
        3
        """
        included = ''
        longest = cur =  0
        for char in s:
            if char in included:
                ind = included.index(char)
                cur -= ind
                included = included[ind+1:]+char
                continue
                
                
            included += char
            cur += 1
            longest = max(longest, cur)
        return longest
            

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)