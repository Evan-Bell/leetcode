class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        >>> s = [1,2,3,4,5,6,7]
        >>> Solution().rotate(s, 3)
        >>> s==[5, 6, 7, 1, 2, 3, 4] 
        True
        """
        k = k%len(nums)
        for i,val in enumerate(nums[-k:] + nums[:-k]):
            nums[i] = val
            

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)