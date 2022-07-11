class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        >>> Solution().firstUniqChar("leetcode")
        0
        >>> Solution().firstUniqChar("loveleetcode")
        2
        """
        seen = {}
        for char in s:
            if(char in seen):   
                seen[char] += 1
            else:
                seen[char] = 1
        for char in s:
            if(seen[char] == 1):
                return s.index(char)
        return -1
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)