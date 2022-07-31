class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        >>> Solution().searchInsert([1,3,5,6], 5)
        2
        >>> Solution().searchInsert([1,3,5,6], 2)
        1
        >>> Solution().searchInsert([1,3,5,6], 7)
        4
        """
        low, high = 0, len(nums)-1
        while low <= high:
            ind = (low + high)//2
            if nums[ind] == target:
                return ind
            if nums[ind] > target:
                high = ind-1
            if nums[ind] < target:
                low = ind+1
        return low
        
        
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)