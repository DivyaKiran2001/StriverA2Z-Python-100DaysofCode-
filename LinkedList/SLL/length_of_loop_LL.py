# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## First we will find the collision point(i.e where both the slow and initialize count as zero fast pointers will meet) then move the fast pointer by one and increase the count value at particular point you
## will reach the same node where the collision happens thats the lenght of the loop of Linkedlist
class Solution:
    def findLengthOfLoop(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next
            if slow==fast:
                return self.countLengthLL(slow,fast)
        return 0
    def countLengthLL(self,slow,fast):
        cnt=1
        fast=fast.next
        while slow!=fast:
            cnt+=1
            fast=fast.next
        return cnt
