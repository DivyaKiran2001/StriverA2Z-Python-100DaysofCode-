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
    
    def delete_at_start(self):
        if self.head is None:
            print("List is empty")
            return
        temp=self.head
        self.head=self.head.next
      
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        # If only one node
        if self.head.next is None:
            self.head = None
            return
        
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
    
    def delete_kth(self,k):
        if self.head is None:
            print("List is empty")
            return
    
        if k==1:
            self.head=self.head.next
        
        cnt=0
        temp=self.head
        prev=None
        while temp is not None:
            cnt+=1
            if cnt==k:
                prev.next=prev.next.next
                break
            prev=temp
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
    
    # print("After deleting at start:")
    # ll.delete_at_start()
    # ll.display()
    
    # print("After deleting at end:")
    # ll.delete_at_end()
    # ll.display()
    
    print("After deleting 2nd element:")
    ll.delete_kth(2)
    ll.display()
    
    
    
