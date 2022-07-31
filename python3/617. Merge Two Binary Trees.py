# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        def merge_tree(r1, r2, m=None):
            if r1 and not r2:
                m = TreeNode(r1.val, merge_tree(r1.left, None), merge_tree(r1.right, None))
            elif r2 and not r1:
                m = TreeNode(r2.val, merge_tree(None, r2.left), merge_tree(None, r2.right))
            elif r1 and r2:
                m = TreeNode(r1.val + r2.val, merge_tree(r1.left, r2.left), merge_tree(r1.right, r2.right))
            return m
        
        return merge_tree(root1, root2)
        
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)