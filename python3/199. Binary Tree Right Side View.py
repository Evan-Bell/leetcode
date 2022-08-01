# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        """
        >>> Solution().rightSideView(TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(5)))
        [1, 5, 4]
        >>> Solution().rightSideView(TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(5,TreeNode(7))))
        [1, 5, 7]
        >>> Solution().rightSideView(TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(5,TreeNode(7,TreeNode(9)))))
        [1, 5, 7, 9]"""
        
        def BFS(node):
            q = [(node,0)]
            out = []
            deepest = -1
            while q:
                curr, depth = q.pop(0)
                if(depth > deepest):
                    deepest = depth
                    out.append(curr.val)
                if curr.right:
                    q.append((curr.right, depth+1))
                if curr.left:
                    q.append((curr.left, depth+1))
            return out
                
                
        if not root:
            return []
        return BFS(root)
            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)