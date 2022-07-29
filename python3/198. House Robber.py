class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        >>> Solution().rob([1,2,3,1])
        4
        >>> Solution().rob([2,7,9,3,1])
        12
        """
        
        n = len(nums)
        if(n<3):
            return max(nums)
        
        nums[n-3] += nums[n-1]
        for i in range(n-4, -1, -1):
            nums[i] += max(nums[i+3], nums[i+2])
        return max(nums[1], nums[0])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)