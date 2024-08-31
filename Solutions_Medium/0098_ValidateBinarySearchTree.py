# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _is_valid_bst(
        self, root: Optional[TreeNode], is_left: bool, caller_val: int
    ) -> bool:
        if root is None:
            return root.val

        if root.left is None and root.right is None:
            return (root.val < caller_val) if is_left else (root.val > caller_val)

        if root.left is not None:
            caller_condition = (
                (root.left.val >= caller_val)
                if is_left
                else (root.left.val <= caller_val)
            )
            if (root.left.val >= root.val) or caller_condition:
                return False
            if not self._is_valid_bst(root.left, is_left=True, caller_val=root.val):
                return False

        if root.right is not None:
            caller_condition = (
                (root.right.val <= caller_val)
                if is_left
                else (root.right.val >= caller_val)
            )
            if (root.right.val <= root.val) or caller_condition:
                return False
            if not self._is_valid_bst(root.right, is_left=False, caller_val=root.val):
                return False

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left_check = self._is_valid_bst(root.left, is_left=True, caller_val=root.val)
        if not left_check:
            return False
        return self._is_valid_bst(root.right, is_left=False, caller_val=root.val)
