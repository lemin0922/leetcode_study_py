# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True

        l_node = root.left if root.left else None
        r_node = root.right if root.right else None

        l_depth, l_isBalance = self.calcDepth(l_node, 0)
        r_depth, r_isBalance = self.calcDepth(r_node, 0)

        return False if abs(l_depth - r_depth) > 1 or not l_isBalance or not r_isBalance else True

    def calcDepth(self, root, n):
        n += 1
        if not root:
            return n - 1, True

        l_node = root.left if root.left else None
        r_node = root.right if root.right else None

        l_depth, l_isBalance = self.calcDepth(l_node, n)
        r_depth, r_isBalance = self.calcDepth(r_node, n)

        depth = max(l_depth, r_depth)
        isBalance = False if abs(l_depth - r_depth) > 1 or not l_isBalance or not r_isBalance else True

        return depth, isBalance