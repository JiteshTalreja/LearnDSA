class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):

        # Case 1 empty list
        if self.head is None:
            return None  # empty list

        # Case 2 only 1 item in list
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value

        # Case 3 more than 1 item in list
        temp = self.head
        while temp.next.next:
            temp = temp.next

        poppedValue = temp.next.value
        temp.next = None
        self.tail = temp
        self.length -= 1
        return poppedValue

    ## From videos

    def pop2(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length +=1
        return True

    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length==0:
            self.tail = None
        return temp

    def get(self, index):
        if index <0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert_value(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index ==self.length:
            return self.append(value)

        temp = self.get(index - 1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True

    def remove(self, index):
        if index<0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index ==self.length:
            return self.pop()

        prev = self.get(index-1)
        temp = prev.next

        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    ## Very, Very common interview questions
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after =temp.next
            temp.next = before
            before = temp
            temp = after
