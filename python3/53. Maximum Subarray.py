class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        >>> Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> Solution().maxSubArray([-2,1])
        1
        >>> Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4,-1,2,1,-5,4])
        7
        """
        total = nums[0]
        maxi = nums[0]
        for i in range(1,len(nums)):
            total += nums[i]
            if(nums[i]>total):
                total = nums[i]
            if(total>maxi):
                maxi=total
        return maxi
        
        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)