# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Using Two pointers Tortoise and Hare Algorithm first we will find if there is any cycle/loop present in the Linked List and then find the starting point
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
        
