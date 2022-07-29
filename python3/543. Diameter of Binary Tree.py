# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        >>> Solution().diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6))))
        4
        """
        
        #@cache
        def height(root):
            if not root:
                return 0
            return max( 1 + height(root.left), 1 + height(root.right))
        
        
        highest = 0
        queue = [root]
        while(queue):
            curr = queue.pop(0)
            if not curr:
                continue
            highest = max(highest, height(curr.left) + height(curr.right))
            queue += [curr.left, curr.right]
        return highest
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)