# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        >>> Solution().maxDepth(TreeNode(1,TreeNode(2),TreeNode(3)))
        2
        """
        if(not root):
            return 0
        return 1 + max(Solution().maxDepth(root.left),Solution().maxDepth(root.right))
        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)