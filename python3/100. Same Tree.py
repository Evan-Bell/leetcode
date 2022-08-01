# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    >>> Solution().isSameTree(TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5)),TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5)))
    True
    >>> Solution().isSameTree(TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5)),TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(6)))
    False
    """
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        queue = [(p,q)]
        while queue:
            p,q = queue.pop(0)
            if p and q:
                if p.val != q.val:
                    return False
            elif p or q:
                return False
            else:
                continue
            queue.append((p.left,q.left))
            queue.append((p.right,q.right))
        return True
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)