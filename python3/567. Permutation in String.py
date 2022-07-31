class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        >>> Solution().checkInclusion("ab", "eidbaooo")
        True
        >>> Solution().checkInclusion("ab", "eidboaoo")
        False
        """
        
        
        oa = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0 }
        
        ob = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0 }
        
        s1_len = len(s1)
        for char in s1:
            oa[char] += 1
        
        for i in range(len(s2)):
            ob[s2[i]] += 1
            if(i >= s1_len):
                ob[s2[i-s1_len]] -= 1
            if oa == ob:
                return True
        return False
            
            
        #---------------------------------------------
        #ARRAY SLIDING WINDOW, WORKS WELL
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        for c in s2[:len(s1)]:
            s2_count[ord(c) - ord('a')] += 1
        if s1_count == s2_count:
            return True
        for i in range(len(s2) - len(s1)):
            s2_count[ord(s2[i]) - ord('a')] -= 1
            s2_count[ord(s2[i + len(s1)]) - ord('a')] += 1
            if s1_count == s2_count:
                return True
        return False
    
    
        #--------------------------------------------------
        #SORTING APPROACH< WORKS BUT SLOW
        s1 = sorted(s1)
        s1_chars = set(s1)
        s1_len = len(s1)
        
        if s1_chars&set(s2) != s1_chars:
            return False
        
        for i in range(len(s2)-s1_len+1):
            if(s2[i] in s1_chars):
                if sorted(s2[i:i+s1_len]) == s1:
                    return True
        return False
            
        
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)