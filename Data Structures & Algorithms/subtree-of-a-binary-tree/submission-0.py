# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)

        def helper(p, q):
            if not p:
                return False
            if isSame(p, q):
                return True
            return helper(p.left, q) or helper(p.right, q)

        return helper(root, subRoot)