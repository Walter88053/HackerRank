class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLinkedList(head):
    n = head
    while n is not None:
        print(n.data, end=" -> ")
        n = n.next
    print("None")

# Creating the linked list
head = Node(16)
second = Node(13)
third = Node(10)
fourth = Node(7)

# Linking the nodes
head.next = second
second.next = third
third.next = fourth

# Printing the elements of the LinkedList
print()
print("The elements of the LinkedList are:")
printLinkedList(head)

