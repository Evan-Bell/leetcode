class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        """
        >>> Solution().topKFrequent(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2)
        ['i', 'love']
        >>> Solution().topKFrequent(['the', 'day', 'is', 'sunny', 'the', 'the', 'the', 'sunny', 'is', 'is'], 4)
        ['the', 'is', 'sunny', 'day']
        """
        res = []
        freq = {}
        occur = {}
        for word in words:
            val = freq.get(word, 0) + 1
            freq[word] = val
            occur[val] = occur.get(val,[]) + [word]
            if(val>1):
                occur[val-1].remove(word)
        
        i = 0
        for each in sorted([key for key in occur])[::-1]:
            if k <= len(occur[each]):
                res += sorted(occur[each])[:k]
                break
            else:
                res += sorted(occur[each])
                k -= len(occur[each])
            
        return res
            
                
        
        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)