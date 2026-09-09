# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        # Gather the list
        array = [head]
        while array[-1].next is not None: array.append(array[-1].next)

        if n == len(array): return head.next
        elif n == 1: array[-n-1].next = None
        else: array[-n-1].next = array[-n+1]

        return head
