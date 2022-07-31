class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        >>> Solution().maxProduct([2,3,-2,4])
        6
        >>> Solution().maxProduct([-2,0,-1])
        0
        >>> Solution().maxProduct([-2,3,-4])
        24
        """
        
        
        #kandane sol
        B = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(nums + B)
    
    
    #--------------------------------------------------
    #MY SOL, WORKS FINE
        best = nums[0]
        maxi, mini = 1,1
        for n in nums:
            if n < 0:
                temp = maxi
                maxi = mini
                mini = temp
            maxi = max(n, n*maxi)
            mini = min(n, n*mini)
            best = max(best, maxi)
        return best
    
    
    #-----------------------------------
    #FAILED SOL, DOESNT WORK
        n = len(nums)
        start,stop = 0, 1
        prod = nums[start]
        largest = 0
        
        while(stop < n and start < n):
            print(prod, start, stop, nums)
            if(nums[stop] == 0):
                start = stop + 1
                stop = start + 2
                prod = nums[start]
            elif(prod / nums[start] > prod):
                prod /= nums[start]
                start += 1
            else:
                prod *= nums[stop]
                stop += 1
            largest = max(largest, prod)
                
        return largest
        
        
        


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)