class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        >>> Solution().twoSum([2,7,11,15], 9)
        [0, 1]
        >>> Solution().twoSum([3,2,4], 6)
        [1, 2]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return None

                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)