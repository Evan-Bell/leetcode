class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        >>> Solution().search([-1,0,3,5,9,12], 9)
        4
        >>> Solution().search([-1,0,3,5,9,12], 2)
        -1
        >>> Solution().search([-1,0,3,5,9,12], -1)
        0
        >>> Solution().search([-1,0,3,5,9,12], 0)
        1
        >>> Solution().search([-1,0,3,5,9,12], 13)
        -1
        >>> Solution().search([-1,0,3,5,9,12], -2)
        -1
        """
        
        #BASIC
        # for each in nums:
        #     if each == target:
        #         return nums.index(each)
        # return -1
    
    
        #BINARY
        high = len(nums)-1
        low = 0
        
        while(low<=high):
            ind = (low+high)//2
            if target == nums[ind]:
                return ind
            elif target > nums[ind]:
                low = ind + 1
            else:
                high = ind - 1
        return -1
            
        

                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)