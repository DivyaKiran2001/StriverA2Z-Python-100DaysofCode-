## Using Merge Sort and Tortoise and Hare Algorithm to find middle of the Linked List for dividing


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMiddle(self,head):
        slow=head
        fast=head
        while(fast is not None and fast.next is not None):
            slow=slow.next
            fast=fast.next.next
        return slow
    def mergeTwoLists(self,l1,l2):
        dummyNode=Node(-1)
        temp=dummyNode
        while l1 and l2:
            if l1.val<=l2.val:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next
        if l1:
            temp.next=l1
        else:
            temp.next=l2
        return dummyNode.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        middle=self.findMiddle(head)
        right=middle.next
        middle.next=None
        left=head
        left=self.sortList(left)
        right=self.sortList(right)
        return self.mergeTwoLists(left,right)

        
