class Solution:
    def getLength(self, head):
        # Your code goes here
        temp=head
        print(temp)
        cnt=0
        while temp is not None:
            temp=temp.next
            cnt+=1
        return cnt

