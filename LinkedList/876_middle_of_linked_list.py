# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        temp1=head
        temp2=head
        while(temp1.next!=None):
            if temp1.next.next!=None:
                temp1=temp1.next.next
                temp2=temp2.next
            else:
                temp1=temp1.next
                temp2=temp2.next
        return temp2
        