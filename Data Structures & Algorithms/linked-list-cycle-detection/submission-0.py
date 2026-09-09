# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        check = set([])
        while (head is not None):
            if head in check:
                return True
            check.add(head)
            head = head.next
        return False