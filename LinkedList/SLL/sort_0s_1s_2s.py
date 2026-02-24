# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def sortList(self, head):
      """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
      """
      zerohead=ListNode(-1)
      onehead=ListNode(-1)
      twohead=ListNode(-1)
      zero=zerohead
      one=onehead
      two=twohead
      temp=head
      while temp is not None:
        if temp.data==0:
          zero.next=temp
          zero=temp
        elif temp.data==1:
          one.next=temp
          one=temp
        else:
          two.next=temp
          two=temp
        temp=temp.next
      zero.next = one.next if one.next else two.next
      one.next = two.next
      two.next = None
      newhead=zerohead.next
      return newhead
