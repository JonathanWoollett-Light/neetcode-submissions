# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [[1,root]]
        most = 1
        while (len(stack) > 0):
            depth, value = stack.pop(0)
            most = max(most, depth)
            if value.left is not None: stack.append([depth + 1, value.left])
            if value.right is not None: stack.append([depth + 1, value.right])
        return most
