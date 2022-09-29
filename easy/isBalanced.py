# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """ ALTERNATIVE SOLUTION
    d = {}
    def getHeight(self, node: Optional[TreeNode]) -> int:
        if not node: return 0
        elif node in self.d: return self.d[node]
        elif not (node.left or node.right):
            self.d[node] = 1
            return 1
        elif not node.left:
            height = self.getHeight(node.right)+1
            self.d[node] = height
            return height
        elif not node.right:
            height = self.getHeight(node.left)+1
            self.d[node] = height
            return height
        else:
            height = max(self.getHeight(node.left), self.getHeight(node.right))+1
            self.d[node] = height
            return height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        if not self.isBalanced(root.left): return False
        if not self.isBalanced(root.right): return False
        
        lH = self.getHeight(root.left)
        rH = self.getHeight(root.right)
        
        if -1 <= (lH - rH) <= 1: return True
        else: return False
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def helper(root: Optional[TreeNode]) -> (int, bool):
            if not root: return (0, True)
            leftHeight, leftBalance = helper(root.left)
            if not leftBalance: return (0, False)
            rightHeight, rightBalance = helper(root.right)
            if not rightBalance: return (0, False)
            if -1 <= (leftHeight - rightHeight) <= 1: return (max(leftHeight, rightHeight) + 1, True)
            else: return (0, False)
        return helper(root)[1]
