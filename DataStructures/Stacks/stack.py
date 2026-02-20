class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):

        temp  =self.top

        while temp:
            print(temp)
            temp = temp.next

    def stack_push(self, value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node
        self.height += 1