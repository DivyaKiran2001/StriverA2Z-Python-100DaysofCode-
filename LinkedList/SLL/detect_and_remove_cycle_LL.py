from typing import *

# Following is the structure of  Node
# Do not update or change the structure 

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

def removeLoop(head :Node) -> Node :

    # Write your code
    if head is None or head.next is None:
        return head
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            fast=head
            while slow.next!=fast.next:
                slow=slow.next
                fast=fast.next
            fast.next=None
    
