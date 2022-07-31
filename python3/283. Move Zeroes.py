class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        >>> s = [0,1,0,3,12]
        >>> Solution().moveZeroes(s)
        >>> s==[1,3,12,0,0]
        True
        """
        
        non_zeros = []
        for val in nums:
            if val != 0:
                non_zeros.append(val)
        
        for i in range(len(nums)):
            if non_zeros:
                nums[i] = non_zeros.pop(0)
            else:
                nums[i] = 0
        return 
    
    
    
    
        #---------------------------------------------------------------
        #SLOW SOL
        def move_back(ind):
            for i,val in enumerate(nums[ind+1:]+[0]):
                nums[i+ind] = val
        i = len(nums)
        while i:
            i -= 1
            if nums[i] == 0:
                move_back(i)
            
        
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)