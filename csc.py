class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Delete a node by key
    def delete_node(self, key):
        current = self.head

        # If head is the node to delete
        if current and current.data == key:
            self.head = current.next
            return

        # Otherwise find the node
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # Key not found
        if not current:
            print(f"{key} not found in list.")
            return

        # Unlink the node
        prev.next = current.next

    # Display list
    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# -------------------------- TEST THE LINKED LIST --------------------------

ll = LinkedList()

# Insert 5 values
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_end(50)

print("Before deleting:")
ll.display_list()         # 10 -> 20 -> 30 -> 40 -> 50 -> None

# Delete one value
ll.delete_node(30)

print("After deleting 30:")
ll.display_list()         # 10 -> 20 -> 40 -> 50 -> None
