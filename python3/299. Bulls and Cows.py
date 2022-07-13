class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = B = 0
        sec_chars = []
        gue_chars = []
        for s,g in zip(secret,guess):
            if s==g:
                A+=1
            else:
                sec_chars.append(s)
                gue_chars.append(g)
        
        for i in range(len(gue_chars)):
            if gue_chars[i] in sec_chars:
                B+=1
                sec_chars.remove(gue_chars[i])
                
        return f"{A}A{B}B"
            
            
        
                
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)