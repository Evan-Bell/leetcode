class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        """
        >>> Solution().threeSumClosest([-1,2,1,-4], 1)
        2
        >>> Solution().threeSumClosest([1,1,1,0], -100)
        2
        """
        nums.sort()
        n = len(nums)
        highest = nums[0]+nums[1]+nums[2]
        for i in range(n):
            j, k = i+1, n-1
            while(k > j):
                total = nums[i] + nums[j] + nums[k]
                if(total == target):
                    return total
                if abs(total-target) < abs(highest-target):
                    highest = total
                    
                if(total < target):
                    j += 1
                if(total > target):
                    k -= 1
        return highest
                    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)