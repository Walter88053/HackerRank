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

# Create the linked list
my_list = LinkedList()

# Append the elements
my_list.append(16)
my_list.append(13)
my_list.append(10)
my_list.append(7)

# Print the linked list
print()
my_list.print_list()

