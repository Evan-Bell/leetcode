class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        >>> Solution().isIsomorphic("egg","add")
        True
        >>> Solution().isIsomorphic("egg","aid")
        False
        """
        s_map = {}
        t_map = {}
        for _s, _t in zip(s,t):
            if ((_s not in s_map) and (_t not in t_map)):
                s_map[_s] = _t
                t_map[_t] = _s
            elif (s_map.get(_s) != _t or t_map.get(_t) != _s):
                return False
        return True

        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)