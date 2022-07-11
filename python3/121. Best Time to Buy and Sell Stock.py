class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        >>> Solution().maxProfit([7,1,5,3,6,4])
        5
        """
        maxi = 0
        sell = 1
        buy = 0
        while(sell<len(prices)):
            if(prices[sell]-prices[buy] > maxi):
                maxi = prices[sell]-prices[buy]
            if(prices[sell]-prices[buy]<0):
                buy = sell
                sell = buy+1
            else:
                sell+=1
        return maxi
        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)