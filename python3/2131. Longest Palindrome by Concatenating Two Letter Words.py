from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        """
        >>> Solution().longestPalindrome(["abcd","dcba","lls","s","sssll"])
        4
        """
        unp = res = 0
        seen = defaultdict(int)
        for each in words:
            if(seen[each[::-1]] > 0):
                res += 4
                seen[each[::-1]] -= 1
                unp -= 1 if each[0] == each[1] else 0
            else:
                seen[each] += 1
                unp += 1 if each[0] == each[1] else 0
                
        return res + (2 if unp > 0 else 0)          
                
            
                

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)