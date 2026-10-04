class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        temp1 = head

        if temp1 == None or temp1.next == None:
            return temp1

        prev = head
        curr = head.next
        prev.next=None

        while curr != None:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp

        head = prev

        return head