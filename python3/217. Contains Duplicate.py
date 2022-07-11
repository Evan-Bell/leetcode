class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        >>> Solution().containsDuplicate([1,2,3,1])
        True
        >>> Solution().containsDuplicate([1,2,3,4])
        False
        """
        if(len(nums) != len(set(nums))):
            return True
        return False
        
        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)