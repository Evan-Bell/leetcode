class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        >>> Solution().lastStoneWeight([2,7,4,1,8,1])
        1
        """
        while(len(stones) > 1):
            stones.sort()
            x = stones.pop()
            y = stones.pop()
            if(x!=y):
                stones.append(abs(x-y))
              
        if(stones):
            return stones[0] 
        return 0
        
        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)