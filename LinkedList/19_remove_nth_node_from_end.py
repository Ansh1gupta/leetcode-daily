# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        slow=head
        fast=head
        if slow==None:
            return head
        else:
            for i in range(n):
                fast=fast.next
            if fast==None:
                head=head.next
            else:
              while(fast!=None and fast.next!=None):
                 slow=slow.next
                 fast=fast.next
              if slow.next!=None:
                 slow.next=slow.next.next
            return head