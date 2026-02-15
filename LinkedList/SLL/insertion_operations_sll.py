class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
    def insert_at_start(self,val):
        if self.head is None:
            print("List is empty")
            return
        temp=Node(val)
        temp.next=self.head
        self.head=temp
    
    def insert_at_last(self,val):
        if self.head is None:
            print("List is empty")
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        newNode=Node(val)
        temp.next=newNode
        
    def insert_at_kth(self,val,k):
        if self.head is None:
            print("List is empty")
            if k==1:
                newNode=Node(val)
                self.head=newNode
        if k==1:
            temp=Node(val)
            self.head=temp
        cnt=0
        temp=self.head
        while temp is not None:
            cnt+=1
            if cnt==k-1:
                newNode=Node(val)
                newNode.next=temp.next
                temp.next=newNode
                
            temp=temp.next
        
        
      
    
        


# Example usage (just structure creation)
if __name__ == "__main__":
    ll = LinkedList()
     # Manually creating nodes
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

    # Linking nodes
    ll.head = node1
    node1.next = node2
    node2.next = node3
    
    print("Original List:")
    ll.display()
    
    print("After inserting at start:")
    ll.insert_at_start(5)
    ll.display()
    
    print("After inserting at last:")
    ll.insert_at_last(35)
    ll.display()
    
    print("After inserting at kth:")
    ll.insert_at_kth(40,2)
    ll.display()
    
    
    
    
