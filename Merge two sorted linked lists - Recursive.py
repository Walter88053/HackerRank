class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def MergeLists(head1, head2):
       # Base cases for recursion
       if head1 is None:
           return head2
       if head2 is None:
           return head1
       # Recursively merge lists
       if head1.data < head2.data:
           head1.next = MergeLists(head1.next, head2)
           return head1
       else:
           head2.next = MergeLists(head1, head2.next)
           return head2


# Helper function to create a linked list from a Python list
def create_linked_list(arr):
    head = None
    for value in reversed(arr):
        node = Node(value)
        node.next = head
        head = node
    return head

# Create two linked lists from Python lists
headA = create_linked_list([x for x in range(997)])
headB = create_linked_list([995, 996])

# Merge the lists
merged_head = MergeLists(headA, headB)

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Print the merged linked list
print()
print_linked_list(merged_head)




