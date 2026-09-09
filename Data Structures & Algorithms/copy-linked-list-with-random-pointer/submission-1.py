"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from copy import copy
# O(n + n)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        new_head = copy(head)
        array = [new_head]
        store = {head: new_head}
        after = head.next

        while after is not None:
            new_after = copy(after)
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


        


        