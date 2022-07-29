# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        #@cache
        def exists_in_tree(curr):
            res = []
            if not curr:
                return []
            if(curr == p):
                res += [2]
            if(curr == q):
                res += [1]
            res += exists_in_tree(curr.left) + exists_in_tree(curr.right)
            return res
        
        queue = [root]
        while(queue):
            curr = queue.pop(0)
            if not curr:
                continue
            l = exists_in_tree(curr.left)
            r = exists_in_tree(curr.right)
            if len(l) == 1 or len(r) == 1:
                return curr 
            if (len(l) == 2):
                queue.append(curr.left)
            if (len(r) == 2):
                queue.append(curr.right)
        return None
        
            
                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)