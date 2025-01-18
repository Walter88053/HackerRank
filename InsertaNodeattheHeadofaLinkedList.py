class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def InsertNodeAtHead(head, data):
    new_node = SinglyLinkedListNode(data)
    new_node.next = head
    return new_node



head = None
head = InsertNodeAtHead(head, 383)
head = InsertNodeAtHead(head, 484)
head = InsertNodeAtHead(head, 392)
head = InsertNodeAtHead(head, 975)
head = InsertNodeAtHead(head, 321)


def print_list(llist):
    current = head
    count = 0
    while current:
        print(current.data, end=" > ")
        current = current.next
        count += 1
    print("None")
    return count

# Print the linked list
print()
node_count = print_list(head)
print(f"This list has {node_count} nodes.")


