'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def findIntersection(firstHead, secondHead):
	# Write your code here.
	# if firstHead is None or secondHead is None:
    #     return None
    t1=firstHead
    t2=secondHead
    while t1!=t2:
        t1=t1.next
        t2=t2.next
        if t1==t2:
            return t1
        if t1 is None:
            t1=secondHead
        if t2 is None:
            t2=firstHead
    return t1
