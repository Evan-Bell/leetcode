class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """
        >>> Solution().pivotIndex([1,7,3,6,5,6])
        3
        >>> Solution().pivotIndex([1,2,3])
        -1
        >>> Solution().pivotIndex([-1,-1,-1,0,1,1])
        0
        >>> Solution().pivotIndex([-1,-1,-1,0,1,1,1])
        -1
        """
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            total -= nums[i]
            if(total == left):
                return i
            left += nums[i]
        return -1
        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)