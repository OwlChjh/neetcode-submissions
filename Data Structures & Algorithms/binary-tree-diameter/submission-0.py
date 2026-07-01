# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0

        def depth(root) -> int: # return height of tree
            if not root:
                return 0

            nonlocal d

            left = depth(root.left)
            right = depth(root.right)

            d = max(d, left + right)
            
            return 1 + max(left, right)

        depth(root)
        return d