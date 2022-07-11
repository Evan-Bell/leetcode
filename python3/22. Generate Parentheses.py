class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        >>> Solution().generateParenthesis(3)
        ['((()))', '(()())', '(())()', '()(())', '()()()']
        
        """
        poss = set(Solution.paren_recurse(self,["("],n))
        results = set()
        dont = set()
        for each in poss:
            if(each in dont or each[-1]!=")"):
                dont.add(each)
                continue
            counter = 0
            for char in each:
                if char == "(":
                    counter += 1
                if char == ")":
                    counter -= 1
                if counter < 0:
                    dont.add(each)
                    break
            if each not in dont:
                results.add(each)
        
        return sorted(list(results))
            
                    
            
    def paren_recurse(self, result, n):
        end = []
        for each in result:
            if each.count("(") > n or each.count(")") > n:
                continue
            end.append(each+"(") 
            end.append(each+")") 
        
        if(len(end[0])==2*n):
            return end
        return Solution.paren_recurse(self,end, n)

                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)