#Optimal Approach 
'''
We use Tortoise and Hare method using fast and slow pointers
(i) First we will find middle of LL for both even and odd number of nodes
(ii) And After finding the middle of the LL now reverse it using Reverse algorithm  and now compare this reverse head nodes with first 
half of the LL to see if they are same if they are same then we can confirm that it is a palindrome or else not
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self,head):
        if head is None or head.next is None:
            return head
        newhead=self.reverseLL(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newhead
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        slow=head
        fast=head
        while fast.next is not None and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
        newhead=self.reverseLL(slow.next)
        first=head
        second=newhead
        while second is not None:
            if first.val!=second.val:
                self.reverseLL(newhead)
                return False
            first=first.next
            second=second.next
        self.reverseLL(newhead)
        return True

        
