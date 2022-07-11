class Solution:
    def isValid(self, s: str) -> bool:
        """
        >>> Solution().isValid("()")
        True
        >>> Solution().isValid("()[]{}")
        True
        >>> Solution().isValid("(]")
        False
        >>> Solution().isValid("([)]")
        False
        
        """
        rels = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        opens = ""
        for char in s:
            if char in "({[":
                opens += char
            else:
                if(not opens):
                    return False
                elif(char != rels[opens[-1]]):
                    return False
                opens = opens[:-1]
        return not opens
        



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)