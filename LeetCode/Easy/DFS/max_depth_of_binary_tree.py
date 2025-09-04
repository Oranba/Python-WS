# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return max(leftDepth,rightDepth)+1

    def test_maxDepth():
        sol = Solution()
        # Test 1: Empty tree
        assert sol.maxDepth(None) == 0, "Test 1 failed"

        # Test 2: Single node
        root = TreeNode(1)
        assert sol.maxDepth(root) == 1, "Test 2 failed"

        # Test 3: Balanced tree
        root = build_tree([1, 2, 3, 4, 5])
        assert sol.maxDepth(root) == 3, "Test 3 failed"

        # Test 4: Unbalanced tree
        root = build_tree([1, 2, None, 3, None, 4])
        assert sol.maxDepth(root) == 4, "Test 4 failed"


        # Helper to build a tree from list (level order)
        def build_tree(nodes):
            if not nodes:
                return None
            root = TreeNode(nodes[0])
            queue = [root]
            i = 1
            while queue and i < len(nodes):
                current = queue.pop(0)
                if nodes[i] is not None:
                    current.left = TreeNode(nodes[i])
                    queue.append(current.left)
                i += 1
                if i < len(nodes) and nodes[i] is not None:
                    current.right = TreeNode(nodes[i])
                    queue.append(current.right)
                i += 1
            return root