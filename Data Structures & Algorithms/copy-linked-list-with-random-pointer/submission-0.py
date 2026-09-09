"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# O(n + n)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        new_head = Node(head.val,head.next,head.random)
        array = [new_head]
        store = {head: new_head}
        after = head.next

        while after is not None:
            new_after = Node(after.val,after.next,after.random)
            array[-1].next = new_after
            store[after] = new_after
            array.append(new_after)
            after = after.next
            
        # print(f"array: {array}")
        # print(f"store: {store}")

        for i in range(len(array)):
            # print(f"{i} before: {array[i].random}")
            if array[i].random is None: continue
            array[i].random = store[array[i].random]
            # print(f"{i} after: {array[i].random} {array[i].val}")

        # print(f"new_head: {new_head}")
        # print(f"array[2].random: {array[2].random}")

        return new_head


        


        