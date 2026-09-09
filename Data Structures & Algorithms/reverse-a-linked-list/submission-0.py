# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        ptrs = [head]
        while ptrs[-1].next is not None:
            ptrs.append(ptrs[-1].next)

        for i in range(1,len(ptrs)):
            ptrs[-i].next = ptrs[-i-1]
        ptrs[0].next = None

        return ptrs[-1]
