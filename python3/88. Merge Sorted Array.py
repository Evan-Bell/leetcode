class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        >>> Solution().merge([1,2,3,0,0,0],3,[2,5,6],3)
        [1, 2, 2, 3, 5, 6]
        >>> Solution().merge([1],1,[],0)
        [1]
        >>> Solution().merge([0],0,[1],1)
        [1]
        """

                
        #fewest lines, built in sort
        # [nums1.pop() for i in range(m+n) if i>=m]
        # nums1.extend(nums2)
        # nums1.sort()
        
        
        #add in, then bubble sort
#         for i in range(n):
#             nums1[m+i] = nums2[i]
        
#         for j in range(1,m):
#             swapped = False
#             for i in range(m-j):
#                 if(nums1[i] > nums1[i+1]):
#                     temp = nums1[i]
#                     nums1[i] = nums1[i+1]
#                     nums1[i+1] = temp
#                     swapped = True
#             if(not swapped):
#                 break


        index = 0
        for num in nums2:
            for i in range(index, m+n):
                if(num < nums1[i] or i == len(nums1)-n):
                    nums1.insert(i,num)
                    index = i
                    break
                
        
        [nums1.pop() for i in range(n)]
        return nums1
        

        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)