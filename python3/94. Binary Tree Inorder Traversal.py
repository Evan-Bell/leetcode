# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        
        #RECURSIVE SOL
        if(not root):
            return []
        
        return Solution().inorderTraversal(root.left) + [root.val] + Solution().inorderTraversal(root.right)
        
        #NON-RECURSIVE SOL
#         res = []
#         queue = []
#         while(queue or root):
#             while(root):
#                 queue.append(root)
#                 root = root.left
#             root = queue.pop()
#             res.append(root.val)
#             root = root.right
#         return res



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)