class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Delete at start
    def delete_at_start(self):
        if self.head is None:
            print("List is empty")
            return
        
        # If only one node
        if self.head.next is None:
            self.head = None
            return
        prev2=self.head
        self.head=self.head.next
        self.head.prev=None
        prev2.next=None
        # self.head = self.head.next
        # self.head.prev = None

    # Delete at end
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        
        # If only one node
        if self.head.next is None:
            self.head = None
            return
        
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        
        prev2=tail.prev
        prev2.next=None
        tail.prev=None
        
        

    # Delete kth node (1-based indexing)
    def delete_kth(self, k):
        if self.head is None:
            print("List is empty")
            return
        
        if k == 1:
            self.delete_at_start()
            return
        
        temp = self.head
        count = 1
        
        while temp is not None and count < k:
            temp = temp.next
            count += 1
        
        # If k is greater than length
        if temp is None:
            print("Position out of range")
            return
        
        # If deleting last node
        if temp.next is None:
            temp.prev.next = None
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

    dll.head = node1
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2

    print("Original List:")
    dll.display()

    print("After deleting 2nd element:")
    dll.delete_kth(1)
    dll.display()
