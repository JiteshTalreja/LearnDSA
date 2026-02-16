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

    def prepend(self, value):

        newNode = Node(value)

        if self.length == 0:
            self.head = self.tail = newNode

        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1
        return True

    def pop_first(self):

        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):

        if index <0 or index > self.length:
            return None
        if index < self.length //2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp


