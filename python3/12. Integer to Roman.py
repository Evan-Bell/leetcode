class Solution:
    def intToRoman(self, num: int) -> str:
        """
        >>> Solution().intToRoman(3)
        'III'
        >>> Solution().intToRoman(4)
        'IV'
        >>> Solution().intToRoman(9)
        'IX'
        >>> Solution().intToRoman(58)
        'LVIII'
        >>> Solution().intToRoman(1994)
        'MCMXCIV'

        """
        vals = [(1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"), (40, "XL"), (50, "L"), (90, "XC"), (100, "C"), (400, "CD"), (500, "D"), (900, "CM"), (1000, "M")]
        ans = ""
        while(num>0):
            if(num < vals[-1][0]):
                vals.pop()
                continue
            for i in range(num//vals[-1][0]):
                ans += vals[-1][1]
            num = num%vals[-1][0]


        return ans

                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)