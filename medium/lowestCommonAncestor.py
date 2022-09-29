# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pStr = ''
        qStr = ''
        def findP(currTree: 'TreeNode'):
            if not currTree: return False
            elif currTree.val == p: return True
            elif findP(currTree.left: pStr += '0'
            elif findP(currTree.right): pStr += '1'
            
