class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_linked_list(head):
    # This is the iterative approach and is generally preferred
    # due to its simplicity and lower space complexity.

    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

# Helper function to convert a list to a linked list


def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Convert the list to a linked list and call the reverse function


head1 = create_linked_list([1, 2, 3, 4])
head2 = create_linked_list([5, 6, 7, 8])
reversed_head1 = reverse_linked_list(head1)
reversed_head2 = reverse_linked_list(head2)

# Helper function to print the linked list values


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


print()
print_linked_list(reversed_head1)
print_linked_list(reversed_head2)


