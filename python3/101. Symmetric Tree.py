# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preOrder_left(self, root: TreeNode) -> list[int]:
        if(not root):
            return [None]
        return [root.val] + Solution().preOrder_left(root.left) + Solution().preOrder_left(root.right)
    
    def preOrder_right(self, root: TreeNode) -> list[int]:
        if(not root):
            return [None]
        return [root.val] + Solution().preOrder_right(root.right) + Solution().preOrder_right(root.left)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return Solution().preOrder_left(root.left) == Solution().preOrder_right(root.right)

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)