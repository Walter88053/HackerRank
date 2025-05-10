class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to insert an element x into the correct
# position in a sorted singly linked list
def sorted_insert(head, x):
    new_node = Node(x)

    # If the list is empty or x should be inserted at the beginning
    if head is None or x <= head.data:
        new_node.next = head
        return new_node

    # Traverse the list to find the correct position
    curr = head
    while curr.next is not None and curr.next.data < x:
        curr = curr.next

    # Insert the new node
    new_node.next = curr.next
    curr.next = new_node

    return head


def print_list(curr):
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
#    # Create a hardcoded singly linked list:
#    # 3 -> 5 -> 8 -> 10 -> 12
#    head = Node(3)
#    head.next = Node(5)
#    head.next.next = Node(8)
#    head.next.next.next = Node(10)
#    head.next.next.next.next = Node(12)


    # Values for the linked list
    values = [3, 5, 8, 10, 12]

    # Initialize head and previous node
    head = None
    prev_node = None

    for data in values:
        new_node = Node(data)
        if head is None:
            head = new_node  # This is the first node, so set it as head
        else:
            prev_node.next = new_node  # Link previous node to current
            new_node.prev = prev_node  # Link current node back to previous
        prev_node = new_node  # Update previous node

    x = 9
    head = sorted_insert(head, x)
    print()
    print_list(head)
    print(x, "was inserted into this Singly Linked List")
