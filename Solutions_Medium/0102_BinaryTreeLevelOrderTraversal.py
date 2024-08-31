# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _level_order_one_level(self, roots: List[TreeNode]) -> List[int]:
        return [root.val for root in roots]

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        roots_on_level = [root]
        levels = []
        while len(roots_on_level) > 0:
            level = [root.val for root in roots_on_level]
            levels.append(level)
            new_roots = []
            for root in roots_on_level:
                if root.left is not None:
                    new_roots.append(root.left)
                if root.right is not None:
                    new_roots.append(root.right)
            roots_on_level = new_roots

        return levels
