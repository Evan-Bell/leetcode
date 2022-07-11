class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        >>> Solution().isAnagram("egg","add")
        True
        >>> Solution().isAnagram("egg","aid")
        False
        """
        if(len(s)!=len(t)):
            return False
        
        s_seen = {}
        t_seen = {}
        for s_, t_ in zip(s,t):
            if(s_ in s_seen):
                s_seen[s_] += 1
            else:
                s_seen[s_] = 1
            
            if(t_ in t_seen):
                t_seen[t_] += 1
            elif(t_ not in t_seen):
                t_seen[t_] = 1
        
        return s_seen == t_seen
    
    
        #OTHER SOLUTION
        #
        # if(len(s)!=len(t)):
        #     return False
        # for char in set(s):
        #     if(s.count(char) != t.count(char)):
        #         return False
        # return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

