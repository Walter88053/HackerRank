class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for value in lst[1:]:
        current.next = Node(value)
        current = current.next
    return head


def print_linked_list(llist):
    current = llist
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def reverse_and_print(llist):
    prev = None
    current = llist
    # Reverse the linked list
    while current is not None:
        next_node = current.next    # Save the next node
        current.next = prev         # Reverse the link
        prev = current              # Move `prev` to the current node
        current = next_node         # Move to the next node in the list
    current = prev
    # Print the reversed list
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    return prev  # Return the new head of the reversed list


# Example lists
a = [16, 12, 4, 2, 5]
b = [7, 3, 9]
c = [5, 1, 18, 3, 13]

# Convert the Python lists to linked lists
a_ll = create_linked_list(a)
b_ll = create_linked_list(b)
c_ll = create_linked_list(c)

# Reverse and print the linked lists
print("\nList A:")
print_linked_list(a_ll)
print("Reversed List A:")
a_ll = reverse_and_print(a_ll)

print("\nList B:")
print_linked_list(b_ll)
print("Reversed List B:")
b_ll = reverse_and_print(b_ll)

print("\nList C:")
print_linked_list(c_ll)
print("Reversed List C:")
c_ll = reverse_and_print(c_ll)

