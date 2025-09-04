from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            if not root.left and root.right:
                return self.minDepth(root.right)+1
            if root.left and not root.right:
                return self.minDepth(root.left)+1
            else:
                leftDepth = self.minDepth(root.left)
                rightDepth = self.minDepth(root.right)
                return min(leftDepth, rightDepth)+1