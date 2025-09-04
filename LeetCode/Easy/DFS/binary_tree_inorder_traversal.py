from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._inorder_helper(root, result)
        return result

    def _inorder_helper(self, node: Optional[TreeNode], result: List[int]):
        if node is not None:
            if node.left is None and node.right is None:
                result.append(node.val)
            elif node.left is None:
                result.append(node.val)
                self._inorder_helper(node.right, result)
            elif node.right is None:
                self._inorder_helper(node.left, result)
                result.append(node.val)
            else:
                self._inorder_helper(node.left, result)
                result.append(node.val)
                self._inorder_helper(node.right, result)
