class Solution:
    def fib(self, n: int) -> int:
        if not n:
            return 0
        a = 0
        b = 1
        for i in range(n-1):
            temp = b
            b += a
            a = temp
        return b
    
        #RECURSIVE
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
            
            
        
                
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)