class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        >>> Solution().backspaceCompare('ab#c', 'ad#c') # abc -> adc
        True
        >>> Solution().backspaceCompare('ab##', 'c#d#')
        True
        """

        s_chars = []
        t_chars = []
        for i in range(len(s)):
            if s[i]=="#":
                if(s_chars):
                    s_chars.pop()
            else:
                s_chars.append(s[i])
        
        for i in range(len(t)):
            if t[i]=="#":
                if(t_chars):
                    t_chars.pop()
            else:
                t_chars.append(t[i])
                
        return s_chars==t_chars


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)