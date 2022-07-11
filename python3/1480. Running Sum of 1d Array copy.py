class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """
        >>> Solution().runningSum([1,1,1,1,1])
        [1, 2, 3, 4, 5]
        >>> Solution().runningSum([1,1,1,1,1,1])
        [1, 2, 3, 4, 5, 6]
        >>> Solution().runningSum([1,1,1,1,1,1,1])
        [1, 2, 3, 4, 5, 6, 7]
        """
        ans = [0]
        for each in nums:
            ans.append(each+ans[-1])
        return ans[1:]
        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)