class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        >>> Solution().coinChange([1,2,5], 11)
        3
        >>> Solution().coinChange([2], 3)
        -1
        """
        
        #TAKEN FROM DISCUSS, WORKS VERY WELL, DP SOL
        maxi = float('inf')
        dp = [0] + [maxi] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else maxi for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == maxi]
        #------------------------------------
        #FAILED, TOO SLOW
        least = amount//min(coins) + 1
        queue = [(amount,0)]
        while(queue):
            a,cnt = queue.pop(0)
            if a < 0:
                continue
            if a == 0:
                return cnt
            for coin in coins[::-1]:
                queue.append((a-coin, cnt + 1))
        return -1
            
                
        
        #-------------------------------------------------------
        #FAILED, DOESNT WORK
        coins = sorted(coins)
        if amount == 0:
            return 0
        a = 0
        cnt = 0
        while(amount > a and coins):
            print(coins, amount)
            coin = coins.pop()
            cnt += amount//coin
            amount = amount%coin
        
        if(amount == a):
            return cnt
        return -1
            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)