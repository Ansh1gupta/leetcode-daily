''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        temp1=head
        if temp1.next==None:
            return 0
        else:
            temp2=head
            while(temp1!=None and temp1.next!=None):
                temp1=temp1.next.next
                temp2=temp2.next
                if temp1==temp2:
                    count=1
                    temp1=temp1.next
                    while(temp1!=temp2):
                        count+=1
                        temp1=temp1.next
                    return count
            return 0
        