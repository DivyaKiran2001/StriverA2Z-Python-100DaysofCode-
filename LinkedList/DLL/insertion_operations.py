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

    # Insert at start
    def insert_at_start(self, val):
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    # Insert at last
    def insert_at_last(self, val):
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next=newNode
        newNode.prev=temp
        

        # temp.next = newNode
        # newNode.prev = temp

    # Insert at kth position (1-based index)
    def insert_at_kth(self, val, k):
        newNode = Node(val)

        # Insert at position 1
        if k == 1:
            if self.head is not None:
                newNode.next = self.head
                self.head.prev = newNode
            self.head = newNode
            return

        temp = self.head
        count = 1

        while temp is not None and count < k - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        newNode.next = temp.next
        newNode.prev = temp

        if temp.next is not None:
            temp.next.prev = newNode

        temp.next = newNode


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

    print("After inserting at start:")
    dll.insert_at_start(5)
    dll.display()

    print("After inserting at last:")
    dll.insert_at_last(35)
    dll.display()

    print("After inserting at kth (position 2):")
    dll.insert_at_kth(40, 2)
    dll.display()
