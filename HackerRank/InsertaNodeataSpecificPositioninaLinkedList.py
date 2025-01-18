class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeAtPosition(llist, data, position):
    new_node = SinglyLinkedListNode(data)

    # Special case: Insert at the head
    if position == 0:
        new_node.next = llist
        return new_node

    current = llist
    count = 0

    # Traverse the list to find the node just before the target position
    while current is not None and count < position - 1:
        current = current.next
        count += 1

    if current is None:
        raise ValueError("Position is out of bounds.")

    # Insert the new node
    new_node.next = current.next
    current.next = new_node

    return llist


# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Create a sample linked list: 16 -> 13 -> 7
head = SinglyLinkedListNode(16)
node2 = SinglyLinkedListNode(13)
node3 = SinglyLinkedListNode(7)
head.next = node2
node2.next = node3

# Insert a new node with data 1 at position 2
new_head = insertNodeAtPosition(head, 1, 2)

# Print the updated linked list
print()
print_linked_list(new_head)
