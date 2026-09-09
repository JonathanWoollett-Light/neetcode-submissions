# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        carry = 0
        prev = None
        node = ListNode()
        start = node

        while(l1 is not None and l2 is not None):
            add = l1.val + l2.val + carry
            rem = add % 10
            carry = add // 10
            # print(f"{add} {rem} {carry}")

            # Update sum
            node.val = rem
            if prev is not None: prev.next = node

            # Step along
            prev = node
            node.next = ListNode()
            node = node.next
            l1 = l1.next
            l2 = l2.next

        while(l1 is not None):
            add = l1.val + carry
            rem = add % 10
            carry = add // 10
            # print(f"l1 {add} {rem} {carry}")

            node.val = rem
            prev = node
            node.next = ListNode()
            node = node.next
            l1 = l1.next

        while(l2 is not None):
            add = l2.val + carry
            rem = add % 10
            carry = add // 10
            # print(f"l2 {add} {rem} {carry}")

            node.val = rem
            prev = node
            node.next = ListNode()
            node = node.next
            l2 = l2.next
        
        if carry == 0: prev.next = None
        else: node.val = int(carry)
        # if node.val == 0: prev.next = None
        return start