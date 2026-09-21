# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack = None
        q_stack = None

        if p is None and q is None: return True
        elif p is not None and q is not None: 
            p_stack = [p]
            q_stack = [q]
        else: return False

        while (p_stack):
            p = p_stack.pop()
            q = q_stack.pop()

            if p.val != q.val: return False

            if p.left is not None:
                if q.left is None: return False
                p_stack.append(p.left)
                q_stack.append(q.left)
            elif p.left is None and q.left is not None: return False
            if p.right is not None:
                if q.right is None: return False
                p_stack.append(p.right)
                q_stack.append(q.right)
            elif p.right is None and q.right is not None: return False
        return True
        