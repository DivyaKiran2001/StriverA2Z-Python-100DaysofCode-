# Approach 1 : Using Iterative Approach
''' Iterative Approach:
Use two pointers: prev (starts as null) and curr (starts at head).
At each step:
1 . Store curr.next in temp.
2 . Reverse curr.next to point to prev.
3 . Move prev to curr and curr to temp.
Repeat until curr is null.
prev becomes the new head of the reversed list.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        temp=head
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev


# Approach 2 : Using Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newhead=self.reverseList(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newhead

        
