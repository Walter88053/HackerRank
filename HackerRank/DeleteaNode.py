class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_node(self, position):
        if self.head is None:  # If the list is empty
            return

        # Handle special case for deleting the last node
        if position == -1:
            # Find the second-to-last node
            current = self.head
            if current.next is None:  # If there's only one node
                self.head = None
                return
            while current.next and current.next.next:
                current = current.next
            current.next = None
            return

        # If the head node is to be deleted
        if position == 0:
            self.head = self.head.next
            return

        # Traverse the list to find the node just before the one to delete
        current = self.head
        count = 0
        while current is not None and count < position - 1:
            current = current.next
            count += 1

        # If the position is greater than the number of nodes
        if current is None or current.next is None:
            return

        # Delete the node
        current.next = current.next.next


# Create the linked list
my_list = LinkedList()

# Append the elements
for data in [8, 20, 6, 2, 19, 7, 4, 15, 9, 3]:
    my_list.append(data)

# Print the linked list
print("\nOriginal list:")
my_list.print_list()


# Delete the last node dynamically
my_list.delete_node(0)   # Delete the first node
my_list.delete_node(3)   # Delete the node at position 3
my_list.delete_node(-1)  # Delete the last node


# Print the linked list after deletion
print("\nNew list after deleting the first node, the node at position 3, and the last node:")
my_list.print_list()

