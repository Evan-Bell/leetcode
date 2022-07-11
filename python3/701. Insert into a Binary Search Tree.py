# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        def insert(root, val):
            if(not root):
                root = TreeNode(val)
                return root
            if(root.val > val):
                return TreeNode(root.val, insert(root.left, val),root.right )
            elif(root.val < val):
                return TreeNode(root.val,root.left,insert(root.right, val) )
        
        return insert(root, val)
            
                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)