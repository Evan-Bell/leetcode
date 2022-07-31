class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """
        >>> Solution().canPartition([1,5,11,5])
        True
        >>> Solution().canPartition([1,2,3,5])
        False
        """
        
        #@cache
        def subSum(s, i):
            if s == 0: 
                return True
            if i >= len(nums) or s < 0: 
                return False
            return subSum(s-nums[i], i+1) or subSum(s, i+1)
        total_sum = sum(nums)
        return total_sum & 1 == 0 and subSum(total_sum // 2, 0)
    
    
    
        #----------------------------------------------
        #FAILED SOL, TOO LONG
        n = len(nums)
        def part(i=0, left=0, right=0):
            if i >= n:
                return left == right
            return part(i+1, left + nums[i], right) or part(i+1, left, right + nums[i])
        return part()
        
        
        #-----------------------------------------------------------------------
        #FAILED SOL, DOESNT WORK
        nums = sorted(nums)
        total, left = 0, sum(nums)
        for n in nums:
            total += n
            left -= n
            if(left == total):
                return True
        return False
        


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)