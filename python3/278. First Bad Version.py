# The isBadVersion API is already defined for you.
#def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n
        while(start <= end):
            ind = (end+start)//2
            if isBadVersion(ind):
                end = ind-1
            else:
                start = ind + 1
        return start
            
        

                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)