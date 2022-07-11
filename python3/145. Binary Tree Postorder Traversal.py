# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        """
        >>> Solution().postorderTraversal(TreeNode(1,TreeNode(2),TreeNode(3)))
        [2,3,1]
        """
        
        #RECURSIVE SOL
#         if not root:
#             return []
        
#         return Solution().postorderTraversal(root.left) + Solution().postorderTraversal(root.right) + [root.val]
    
        if(not root):
            return []
        queue = [root]
        res = []
        while(queue):
            cur = queue[-1]
            if(cur.left):
                queue.append(cur.left)
                cur.left = None
            elif(cur.right):
                queue.append(cur.right)
                cur.right = None
            else:
                res.append(cur.val)
                queue.pop()
        return res


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)