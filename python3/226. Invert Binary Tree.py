# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if(not root):
            return None
        temp = root.left
        root.left = Solution().invertTree(root.right) 
        root.right = Solution().invertTree(temp) 
        return root
        

                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)