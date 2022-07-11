# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        """
        >>> Solution().preorderTraversal(TreeNode(1,TreeNode(2),TreeNode(3)))
        [1, 2, 3]
        """
        
        #RECURSIVE SOL
        # if(not root):
        #     return []
        # return [root.val] + Solution().preorderTraversal(root.left) + Solution().preorderTraversal(root.right)
    
        queue, res = [root], []
        
        while queue:
            cur = queue.pop()
            
            if cur:
                res.append(cur.val)
                queue += [cur.right, cur.left]
                
        return res



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)