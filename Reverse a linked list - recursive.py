class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


#   The recursive method, while less space-efficient, can be more intuitive.
def reverse_linked_list(head):
    if not head or not head.next:
        return head
    new_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return new_head

#    Helper function to convert a list to a linked list


def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

#   Convert the list to a linked list and call the reverse function


head1 = create_linked_list([1, 2, 3, 4])
head2 = create_linked_list([5, 6, 7, 8])
reversed_head1 = reverse_linked_list(head1)
reversed_head2 = reverse_linked_list(head2)


#   Helper function to print the linked list values


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


print()
print_linked_list(reversed_head1)
print_linked_list(reversed_head2)



