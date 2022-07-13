# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode ) -> bool:
        def get_Nodes(root):
            if not root:
                return []
            return get_Nodes(root.left) + [root.val] + get_Nodes(root.right)
        
        inOrder = get_Nodes(root)
        prev = inOrder[0]
        for each in inOrder[1:]:
            if prev >= each:
                return False
            prev = each
        return True
                
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)