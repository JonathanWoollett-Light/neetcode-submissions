# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        stack = [(root,False)]
        heights = {None: 0}
        while stack:
            node, expanded = stack.pop()
            if node is None: continue
            if not expanded:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
            else:
                lh, rh = heights[node.left], heights[node.right]
                if abs(lh-rh) > 1: return False
                heights[node] = 1 + max(lh,rh)
        return True