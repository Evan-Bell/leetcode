# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    >>> Solution().isBalanced(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7))))
    True
    >>> Solution().isBalanced(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5), TreeNode(6))), TreeNode(7)))
    False
    """
    def isBalanced(self, root: TreeNode) -> bool:
        def look_down(root):
            if not root:
                return 0
            return 1 + max(look_down(root.left), look_down(root.right))
        
        queue = [root]
        while(queue):
            curr = queue.pop(0)
            if not curr:
                continue
            
            if(abs(look_down(curr.left)-look_down(curr.right)) > 1):
                return False
            queue += [curr.left, curr.right]
        
        return True
        
       

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)