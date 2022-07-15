class Solution:
    def decodeString(self, s: str) -> str:
        """
        >>> Solution().decodeString('2[abc]3[cd]ef')
        'abcabccdcdcdef'
        >>> Solution().decodeString('3[a]2[bc]')
        'aaabcbc'
        >>> Solution().decodeString('3[a2[c]]')
        'accaccacc'
        >>> Solution().decodeString('3[a]2[b4[F]c]')
        'aaabFFFFcbFFFFc'
        """
        def find_brackets(s):
            cnt = 0
            for i in range(len(s)):
                if s[i] == "[":
                    cnt += 1
                if s[i] == "]":
                    cnt -= 1
                if cnt == 0:
                    return i
            return 0
                
                
        if("[" not in s):
            return s
        res = ""
        while(s):
            if(s[0] in "0123456789"):
                first = s.index("[")
                end = find_brackets(s[first:])+first
                res += self.decodeString(s[first+1:end])*int(s[:first])
                s = s[end+1:]
            else:
                res += s[0]
                s = s[1:]
        return res

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)