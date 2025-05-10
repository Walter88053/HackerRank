class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def MergeLists(head1, head2):
    dummy = ListNode()  # Dummy node to simplify the logic
    tail = dummy

    while head1 and head2:
        if head1.data < head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next  # Move the tail forward

    # Attach the remaining nodes from either list
    tail.next = head1 if head1 else head2

    return dummy.next  # Return the merged list, skipping the dummy node



# Helper function to create a linked list from a Python list
def create_linked_list(arr):
    head = None
    for value in reversed(arr):
        node = ListNode(value)
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




