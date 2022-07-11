"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        """
        >>> Solution().preorder(Node(1, [Node(3, [Node(5)]), Node(2), Node(4)]))
        [1, 3, 5, 2, 4]
        >>> Solution().preorder(Node(1, [Node(3), Node(2), Node(4)]))
        [1, 3, 2, 4]
        """

        
        if(not root):
            return []
        
        output = []
        queue = [root]
        while(queue):
            f = queue[-1]
            del queue[-1]
            if(f.children):
                for child in f.children[::-1]:
                    queue.append(child)
            output += [f.val]
        return output
        
        
        
        #RECURSIVE SOLUTION
        # if(not root):
        #     return []
        # output = [root.val]
        # for child in root.children:
        #     output += Solution().preorder(child)
        # return output
                

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)