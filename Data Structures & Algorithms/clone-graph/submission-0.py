"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Return a deep copy of a graph from a root
# It may have cycles so will need to use something like floodfill to cover the graph without cycling
# A grid is just an undirected graph so its the same solution
# Use the `self.val` as the identifier to track if its covered
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None

        old = {}
        new = set([])
        stack = [node]
        while (stack):
            old_n = stack.pop()

            # We only care about covering old nodes, so we skip new ones.
            if old_n in new: continue

            # If we consider a grid or just a simple strip we might consider when
            # 0 is the first old encountered, the new 0 will be created but it
            # will still point to the old 1 since the new 1 hasn't been created.
            # So to make sure the new 0 points to the new 1, when we reach the
            # old 1 we need to both point it at any new values and make its
            # neighbours point at new values (in case it explored its neighbors
            # before exploring here) so that new 0 points to new 1.
            # Basically we need to account for uncertain exploration order.
            
            new_nbrs = [old.get(x,x) for x in old_n.neighbors] # New neighbors
            new_n = Node(old_n.val, new_nbrs) # New node
            old[old_n] = new_n # Old to new map

            # Update neighbors neighbors
            for nbr in new_nbrs:
                if nbr in new: # Only update values of new nodes
                    nbr.neighbors = [new_n if x is old_n else x for x in nbr.neighbors]
            
            new.add(new_n) # Track new node to avoid cycling

            stack += [x for x in new_nbrs if x not in new] # Push old nodes to explore

        return old[node]
        

