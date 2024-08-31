# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseFlipped(self, root: Optional[TreeNode]) -> list[TreeNode]:
        if root is None:
            return []

        return (
            root.val,
            self.traverseFlipped(root.right),
            self.traverseFlipped(root.left),
        )

    def traverse(self, root: Optional[TreeNode]) -> list[TreeNode]:
        if root is None:
            return []

        return root.val, self.traverse(root.left), self.traverse(root.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None:
            return root.right is None

        return self.traverse(root.left) == self.traverseFlipped(root.right)
