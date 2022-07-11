class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        >>> Solution().canConstruct("a", "b")
        False
        >>> Solution().canConstruct("aa", "ab")
        False
        >>> Solution().canConstruct("aa", "aab")
        True
        """
        
        magazine = list(magazine)
        if(len(ransomNote) > len(magazine)):
            return False
        for char in ransomNote:
            if char in magazine:
                magazine.remove(char)
            else:
                return False
        return True
        


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

