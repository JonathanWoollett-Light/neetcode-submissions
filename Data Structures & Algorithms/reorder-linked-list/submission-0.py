# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return

        array = [head]
        while (array[-1].next is not None):
            array.append(array[-1].next)

        # print([x.val for x in array])

        front = 0
        back = len(array) - 1
        # print(f"{front} {back}")
        # 1,2,3,4,5,6
        while(front < back - 1):
            # print(f"{front}->{array[front].val}, {back}->{array[back].val}")
            temp = array[front].next # 2, 3
            array[front].next = array[back] # 1->6, 2->5
            array[back].next = temp # 6->2, 5->3, 
            front += 1
            back -= 1
        array[back].next = None