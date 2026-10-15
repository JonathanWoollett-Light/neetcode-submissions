# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None: return False
        if subRoot is None: return False

        # dfs to get all the potential starts.
        stack = [root]
        starts = []
        while(stack):
            top = stack.pop()
            if top.val == subRoot.val:
                starts.append(top)
            if top.left is not None: stack.append(top.left)
            if top.right is not None: stack.append(top.right)

        # dfs across all starts removing when they mismatch the subroot we are searching for.
        stacks = [[start] for start in starts]
        substack = [subRoot]
        while substack:
            sub = substack.pop()
            if sub.left is not None: substack.append(sub.left)
            if sub.right is not None: substack.append(sub.right)

            i = 0
            while i < len(stacks):
                x = stacks[i].pop()
                if (x.val != sub.val
                        or (x.left is None) != (sub.left is None)
                        or (x.right is None) != (sub.right is None)
                    ):
                    stacks.pop(i)
                    continue
                if x.left is not None: stacks[i].append(x.left)
                if x.right is not None: stacks[i].append(x.right)
                i += 1
            if not stacks: return False
        return True
