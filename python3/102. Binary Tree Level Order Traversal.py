# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """
        >>> Solution().levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
        [[3], [9, 20], [15, 7]]
        """
        if(not root):
            return []
        
        output = [[root.val]]
        queue = [root]
        while (queue):
            cur = []
            for i in range(len(queue)):
                f = queue[0]
                del queue[0]
                if(f.left):
                    queue.append(f.left)
                    cur.append(f.left.val)
                if(f.right):
                    queue.append(f.right)
                    cur.append(f.right.val)
            if(cur):
                output.append(cur)
        return output
                
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)