def romanToInt(s: str) -> int:
    """_summary_

    Args:
        s (str): _description_

    Returns:
        int: _description_
    
    >>> romanToInt('III')
    3
    >>> romanToInt('IV')
    4
    >>> romanToInt('IX')
    9
    >>> romanToInt('LVIII')
    58
    >>> romanToInt('MCMXCIV')
    1994
    """
    chars = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    sum = 0
    for i in range(len(s)-1, -1, -1):
        if(i>0 and chars[s[i]] > chars[s[i-1]]):
            sum += (chars[s[i]]-chars[s[i-1]])-chars[s[i-1]]
        else:
            sum += chars[s[i]]
    return sum


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

