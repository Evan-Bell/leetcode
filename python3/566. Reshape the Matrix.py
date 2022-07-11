class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        """
        >>> 
        """
        if(r*c != len(mat[0])*len(mat)):
            return mat
        i=0
        res = [[] for g in range(r)]
        for row in mat:
            for item in row:
                res[i//c].append(item)
                i+=1
        
        return res
            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)