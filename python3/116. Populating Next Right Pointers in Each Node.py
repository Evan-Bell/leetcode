"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        
        head = root
        def BFS(node):
            q = [(node,0)]
            while q:
                curr,depth = q.pop(0)
                if q:
                    if q[0][1] == depth:
                        curr.next = q[0][0]
                if curr.left:
                    q.append((curr.left, depth+1))
                if curr.right:
                    q.append((curr.right, depth+1))
        
        if not root:
            return root
        BFS(root)
        return head
                    

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


    