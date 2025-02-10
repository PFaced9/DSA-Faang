# Defining Singly Linked List
class SinglyLinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


# Displaying Linked List
    def display(self, head):
        curr = head
        linkedlist = []
        while curr:
            linkedlist.append(str(curr.val))
            curr = curr.next
        print(' -> '.join(linkedlist))

# Search Value

    def search(self, head, val):
        curr = head
        while curr:
            if val == curr.val:
                return True
            curr = curr.next
        return False




Head = SinglyLinkedList(0)
A = SinglyLinkedList(1)
B = SinglyLinkedList(2)
C = SinglyLinkedList(3)
D = SinglyLinkedList(4)

Head.next = A
A.next = B 
B.next = C
C.next = D


# Traversing The List

curr = Head
while curr:
    print(curr)
    curr = curr.next


# A.display(head=Head)
Head.search(Head, 2)