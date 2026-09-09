# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # Explore
        stack = [[[], root]]
        positions = []
        while (len(stack) > 0):
            path, current = stack.pop(0)
            if current.left is not None: stack.append([path + ['l'],current.left])
            if current.right is not None: stack.append([path + ['r'],current.right])
            positions.append(path)
        # print(positions)

        # Find largest combination
        diameter = 0
        for i in range(len(positions)):
            j = i + 1
            while j < len(positions):
                # Trace the shared path
                shared = 0
                for k in range(min(len(positions[i]), len(positions[j]))):
                    if positions[i][k] != positions[j][k]: break
                    shared = k + 1
                
                
                distance = (len(positions[i]) - shared) + (len(positions[j]) - shared) # Add the diverging paths
                diameter = max(diameter, distance) # Set max distance

                # print(f"{positions[i]} -> {positions[j]}: {shared} {distance}")

                j += 1 # Increment

        return diameter
        