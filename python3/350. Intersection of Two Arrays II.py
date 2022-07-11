class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        >>> Solution().intersect([1,2,2,1], [2,2])
        [2, 2]
        """
        res = []
        dont = set()
        for each in nums1:
            n2c = nums2.count(each)
            if(each not in dont and n2c>0):
                res = res + [each]*min(n2c, nums1.count(each))
                dont.add(each)
        return res
        

        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)