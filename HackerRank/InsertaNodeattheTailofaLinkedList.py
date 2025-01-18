class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def InsertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    if head is not None:
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head
    return new_node

# Initialize an empty list
head = None

# Append the elements
head = InsertNodeAtTail(head, 141)
head = InsertNodeAtTail(head, 302)
head = InsertNodeAtTail(head, 164)
head = InsertNodeAtTail(head, 530)
head = InsertNodeAtTail(head, 474)

# Function to print the linked list
# def print_list(head):
#    current = head
#    while current:
#        print(current.data, end=" > ")
#        current = current.next
#    print("None")

def print_list(head):
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
#

# Print the linked list
#print()
#print("This list has x nodes: ", head)
#print_list(head)
#









#def InsertNodeAtTail(head, data):
#    new_node = SinglyLinkedListNode(data)
#    if head is not None:
#        current = head
#        while current.next:
#            current = current.next
#        current.next = new_node
#        return head
#    return new_node
#
#
#
#my_list = InsertNodeAtTail()
#
## Append the elements
#my_list.append(141)
#my_list.append(302)
#my_list.append(164)
#my_list.append(530)
#my_list.append(474)
#
## Print the linked list
#print()
#my_list.print_list()
#
#