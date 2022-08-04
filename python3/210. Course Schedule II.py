from collections import defaultdict
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites:list[list[int]]) -> list[int]:
        """
        >>> Solution().findOrder(2, [[1,0]])
        [0, 1]
        >>> Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
        [0, 1, 2, 3]
        >>> Solution().findOrder(2, [[1,0],[0,1]])
        []
        """
        
        #GREAT SOL, WORKS WELL
        graph = defaultdict(list)
        connections = {}
        
        for i in range(numCourses):
            connections[i] = 0
        
        for i, j in prerequisites:
            graph[j] += [i]
            connections[i] += 1
            
        
        q = deque()
            
        for key, val in connections.items():
            if val == 0:
                q.append(key)
            
        output = []
        
        while q:
            curr = q.popleft()
            output.append(curr)
            for node in graph[curr]:
                connections[node] -= 1
                if connections[node] == 0:
                    q.append(node)
        
        return output if len(output) == numCourses else []        
        
        
        #--------------------------------------------
        #SOL IS BAD, TOO SLOW
        prereq = defaultdict(set)
        courses = list(set([pre for [course,pre] in prerequisites]))
        
        for p in prerequisites:
            if(p[0] in prereq[p[1]]):
                return []
            prereq[p[0]].add(p[1])
            
            
        if not courses:
            return [i for i in range(numCourses)]
        
        for c in courses:
            if(not prereq[c]):
                path = [c]
                flag = True
                while(flag):
                    flag = False
                    for key, val in prereq.items():
                        if val&set(path) == val and key not in path:
                            flag = True
                            path += [key]
                if(len(path) >= len(courses)):
                    return path + [i for i in range(numCourses) if i not in path]
        return []
        
        
        #FAILED TWO, DOESNT PASS CASE OF RECURRING LINKS
        
        def DFS(path):
            res = []
            print(path)
            if path[-1] not in prereq:
                return []
            for c in prereq[path[-1]]:
                if c not in path:
                    temp = DFS([c])
                    if temp:
                        res += temp
                    else:
                        res.insert(0,c)
            return path + res
        
   
        
        for c in courses:
            t = DFS([c])
            print(t)
                
            if len(t) == numCourses:
                return t
        return []
    
    
    
    
    
    
    
        
        #-------------------------------------------------------------
        #FAILED 
        print(prereq, prerequisites)
        
        def DFS(path):
            print(path)
            res = []
            if path[-1] not in course:
                return []
            
            res += list(course[path[-1]])
            for c in course[path[-1]]:
                if(c not in path):
                    res += DFS(path+[c])
            return res
        
        for c in pre:
            t = DFS(c)
            if t:
                return t
        return []
        
                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)