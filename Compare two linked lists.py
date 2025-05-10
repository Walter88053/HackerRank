class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def compare_lists(llist1, llist2):
    while llist1 and llist2:
        if llist1.data != llist2.data:
            return False
        llist1 = llist1.next
        llist2 = llist2.next

        # Check if both lists are of the same length
    if (not llist1 and llist2) or (llist1 and not llist2):
        return False

    return True

    # Helper function to create a linked list from a Python list
def create_linked_list(arr):
    head = Node(arr[0])
    current = head
    for elem in arr[1:]:
        current.next = Node(elem)
        current = current.next
    return head


    # Test the function with linked lists
llist1 = create_linked_list([1, 2, 3])
llist2 = create_linked_list([1, 2, 3, 4])
print()
print(compare_lists(llist1, llist2))  # Should print False

llist1 = create_linked_list([1, 2, 3])
llist2 = create_linked_list([1, 7, 3])
print()
print(compare_lists(llist1, llist2))  # Should print False

llist1 = create_linked_list([1, 2, 3])
llist2 = create_linked_list([1, 2, 3])
print()
print(compare_lists(llist1, llist2))  # Should print True



