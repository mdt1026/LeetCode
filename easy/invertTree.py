# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack[0]
            stack = stack[1:]
            if not node: continue
            stack += [node.left, node.right]
            node.left, node.right = node.right, node.left
        return root
