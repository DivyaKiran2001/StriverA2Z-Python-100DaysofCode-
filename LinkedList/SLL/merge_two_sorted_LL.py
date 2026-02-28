# Optimal Approach using the concept of Two pointer with DummyNode concept



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1=list1
        t2=list2
        dummyNode=ListNode(-1)
        temp=dummyNode
        while t1 is not None and t2 is not None:
            if t1.val<t2.val:
                temp.next=t1
                temp=t1
                t1=t1.next
            else:
                temp.next=t2
                temp=t2
                t2=t2.next
        if t1:
            temp.next=t1
        else:
            temp.next=t2
        return dummyNode.next
        
