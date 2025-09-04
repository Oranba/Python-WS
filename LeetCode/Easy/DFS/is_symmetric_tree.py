class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            return self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)
        return False

    # def is_mirror(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
    #     if not t1 and not t2:
    #         return True
    #     if not t1 or not t2:
    #         return False
    #     return (t1.val == t2.val) and self.is_mirror(t1.right, t2.left) and self.is_mirror(t1.left, t2.right)