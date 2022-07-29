# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """
        >>> Solution().pathSum(TreeNode(10, TreeNode(5,), TreeNode(-3,None, TreeNode(11))), 8)
        1
        >>> Solution().pathSum(TreeNode(10, TreeNode(5,TreeNode(3,TreeNode(3),TreeNode(-2)),TreeNode(2,None,TreeNode(1))), TreeNode(-3,None, TreeNode(11))), 8)    
        3
        """
        
        
        self.paths = 0
        
        def count_path(curr, path):
            if not curr:
                return
            temp = []
            for p in path:
                temp.append(p+curr.val)
                if p+curr.val == targetSum:
                    self.paths += 1
            temp += [curr.val]
            
            if(curr.val == targetSum):
                self.paths += 1
            
                
            count_path(curr.left, temp)
            count_path(curr.right, temp)
            return
         
            
        count_path(root, [])
        return self.paths
            
                
            
        
                
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)