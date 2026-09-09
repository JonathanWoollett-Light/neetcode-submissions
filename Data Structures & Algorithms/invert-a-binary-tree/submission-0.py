# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # bfs
        stack = [root]
        while len(stack) != 0:
            # normal bfs
            current = stack.pop(0)
            if current.left is not None: stack.append(current.left)
            if current.right is not None: stack.append(current.right)

            # Swap
            temp = current.left
            current.left = current.right
            current.right = temp
                    
        return root

