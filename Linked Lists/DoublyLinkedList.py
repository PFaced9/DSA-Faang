class DoublyLinkedList():
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return (str(self.val))


head = tail = DoublyLinkedList(0)
A = DoublyLinkedList(1)
B = DoublyLinkedList(2)
C = DoublyLinkedList(3)

head.next = A
A.next = B
B.next = C

print(head, tail)

# Displaying The Doubly Linked List.
def display(head):
    curr = head
    linkedlist = []
    while curr:
        linkedlist.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(linkedlist))

display(head=head)

# Inserting At The Start.
def insertAtStart(head, tail, val):
    new_node = DoublyLinkedList(val, next = head)
    head.prev = new_node
    return new_node, tail

head, tail = insertAtStart(head, tail, -1)
display(head)

# Inserting At The End.
