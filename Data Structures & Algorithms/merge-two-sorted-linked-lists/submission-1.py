# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Setup
        if list1 is not None:
            if list2 is not None:
                if list1.val <= list2.val:
                    front = list1
                    list1 = list1.next
                else: 
                    front = list2
                    list2 = list2.next
            else:
                return list1
        elif list2 is not None:
            return list2
        else:
            return None
        cursor = front

        # Loop
        while (True):
            temp = None
            if list1 is not None:
                if list2 is not None:
                    if list1.val <= list2.val:
                        temp = list1
                        list1 = list1.next
                    else: 
                        temp = list2
                        list2 = list2.next
                else:
                    temp = list1
                    list1 = list1.next
            elif list2 is not None:
                temp = list2
                list2 = list2.next
            else:
                cursor.next = None
                return front
            cursor.next = temp
            cursor = temp
        
        # unreachable
