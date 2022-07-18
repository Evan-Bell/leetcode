class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        >>> Solution().multiply("123", "456")
        '56088'
        >>> Solution().multiply("9133", "0")
        '0'
        >>> Solution().multiply("0", "0")
        '0'
        >>> Solution().multiply("0", "1")
        '0'
        >>> Solution().multiply("1", "0")
        '0'
        >>> Solution().multiply("1", "1")
        '1'
        >>> Solution().multiply("1", "2")
        '2'
        """
        nums = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
        
        n1  = 0
        for i in num1:
            n1 = n1*10 + nums[i]
            
        n2  = 0
        for i in num2:
            n2 = n2*10 + nums[i]
            
        return str(n1*n2)
                
        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)