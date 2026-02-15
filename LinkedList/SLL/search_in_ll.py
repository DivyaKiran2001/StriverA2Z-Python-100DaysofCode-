class Solution:
    def searchKey(self, head, key):
        # Your code goes here
        temp=head
        while temp is not None:
            if temp.val ==key:
                return True
            temp=temp.next
        return False
        
