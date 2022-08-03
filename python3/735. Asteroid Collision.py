class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        """
        >>> Solution().asteroidCollision([-2,-1,1,2])
        [-2, -1, 1, 2]
        >>> Solution().asteroidCollision([5,10,-5])
        [5, 10]
        >>> Solution().asteroidCollision([8,-8])
        []
        >>> Solution().asteroidCollision([10,2,-5])
        [10]
        """
        stack = [asteroids.pop(0)]
        for a in asteroids:
            while (stack and stack[-1] > 0 and a < 0):
                if stack[-1] < -a: 
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                a = None
                break
            if a != None:
                stack.append(a)
        return stack
    
    
        #--------------------------------------
        #BAD SOL, NOT CLEAN AT ALL
        n = len(asteroids)
        for i in range(n-2, -1, -1):
            print(i)
            if len(asteroids)>1 and (asteroids[i] > 0 and asteroids[i+1] < 0):
                print(i, asteroids)
                left = asteroids[i]
                right = asteroids[i+1]
                if abs(left) == abs(right):
                    del asteroids[i+1]
                    del asteroids[i]
                    i-=1
                else:
                    if abs(left) > abs(right): 
                        del asteroids[i+1]
                    if abs(left) < abs(right): 
                        del asteroids[i]
        return asteroids
    
        stack = [asteroids.pop(0)]
        for a in asteroids:
            if stack[-1] > 0 and a < 0:
                if abs(stack[-1]) == abs(a):
                    stack.pop()
                else:
                    if abs(stack[-1]) < abs(a): 
                        stack[-1] = a
            else:
                stack.append(a)
        return stack

            
            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)