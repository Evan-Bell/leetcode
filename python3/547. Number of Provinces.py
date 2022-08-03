class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        """
        >>> Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
        2
        >>> Solution().findCircleNum([[1,1,0],[1,1,1],[0,1,1]])
        1
        """
        
        n = len(isConnected)
        self.seen = set()
        
        def BFS(x):
            q = [x]
            while q:
                x = q.pop(0)
                if x in self.seen:
                    continue
                self.seen.add(x)
                for i in range(n):
                    if isConnected[x][i] == 1:
                        q.append(i)
            return 1
        
        total = 0
        for i in range(n):
            if i not in self.seen:
                total += BFS(i)
        return total
                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)