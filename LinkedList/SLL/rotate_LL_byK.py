# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findNthNode(self,temp,k):
        cnt=1
        while temp is not None:
            if cnt==k:
                return temp
            cnt+=1
            temp=temp.next
        return temp
        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        # Calculate the length and find the tail
        length=1
        tail=head
        while tail.next is not None:
            tail=tail.next
            length+=1
        if k%length==0:
            return head
        k=k%length
        tail.next=head
        newlastNode=self.findNthNode(head,length-k)
        head=newlastNode.next
        newlastNode.next=None
        return head


        
