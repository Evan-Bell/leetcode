class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        >>> Solution().twoSum([2,7,11,15], 9)
        [1, 2]
        """
        pairs = {}
        for i, val in enumerate(numbers):
            if val in pairs:
                return [pairs[val]+1,i+1]
            pairs[target-val] = i
        return 
                
        
        
        
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)