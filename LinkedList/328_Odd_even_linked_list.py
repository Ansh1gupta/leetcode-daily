# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        temp1=head
        if temp1==None or temp1.next==None or temp1.next.next==None:
            return head
        else:
            temp=temp1.next
            temp2=temp
            while(temp1!=None and temp2!=None and temp1.next!=None and temp2.next!=None):
                temp1.next=temp2.next
                temp2.next=temp1.next.next
                temp1=temp1.next
                temp2=temp2.next
            temp1.next=temp
            return head


        