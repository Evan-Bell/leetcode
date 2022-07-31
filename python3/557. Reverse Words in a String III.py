class Solution:
    def reverseWords(self, s: str) -> str:
        """
        >>> Solution().reverseWords("the sky is blue")
        'eht yks si eulb'
        """
        
        #FULLY WRITTEN SOL
        words = [""]
        for char in s:
            if char == " ":
                words.append("")
            else:
                words[-1] = char + words[-1]
        
        out = ""
        for w in words:
            out += w + ' '
        return out[:-1]
        
        
        
        #ONE LINE
        return " ".join([i[::-1] for i in s.split(" ")])
        
        
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)