# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """
        >>> Solution().findTarget(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, TreeNode(7))), 9)
        True
        >>> Solution().findTarget(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, TreeNode(7))), 28)
        False
        >>> Solution().findTarget(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, TreeNode(7))), 15)
        False
        """
        comp = set()
        queue = [root]
        while(queue):
            curr = queue.pop(0)
            if not curr:
                continue
            if k - curr.val in comp:
                return True
            comp.add(curr.val)
            queue += [curr.left, curr.right]
        return False
        


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)