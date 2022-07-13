class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        chars = {'a': 0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}

        p_chars = [0]*26
        s_chars = [0]*26
        res = []
        for i in range(len(p)):
            p_chars[chars[p[i]]] += 1;
        
        prev = None
        for i in range(len(s)):
            prev = i-len(p)
            if(prev>=0):
                s_chars[chars[s[prev]]] -= 1
            s_chars[chars[s[i]]] += 1
            if(s_chars == p_chars):
                res.append(i-len(p)+1)
        return res
            
                
        
        
        
        #----------------------------------------------
        #FAILED BELOW #2
        sorted_p = sorted(p)
        s_len = len(s)
        if(len(p)>s_len):
            return []
        res = []
        for i in range(s_len-len(p)+1):
            if(s[i] in p and sorted(s[i:i+len(p)]) == sorted_p):
               res.append(i)
        return res
        
        
        #----------------------------------------------
        #FAILED BELOW #1
        def anagrams(inp, prev):
            if(len(inp) == 1):
                return [prev+inp]
            out = []
            for i in range(len(inp)):
                out += anagrams(inp[:i] + inp[i+1:], prev+inp[i])
            return out
        
        
        if(len(p)>len(s)):
            return []
        res = []
        ana = set(anagrams(p, ""))
        for i in range(len(s)):
            if s[i:i+len(p)] in ana:
                res.append(i)
        return res
   
                
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)