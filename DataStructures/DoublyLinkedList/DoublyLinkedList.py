class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        newNode=  Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def print_dll(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        newNode = Node(value)
        if self.length ==0:
            self.head = newNode
            self.tail = newNode
        if self.length>0:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length +=1
        return True

    def pop(self):
        if self.length ==0:
            return None

        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp



