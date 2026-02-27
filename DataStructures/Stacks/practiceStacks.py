#Stack: Implement Stack Using a List ( ** Interview Question)

class Stack:
    def __init__(self):
        self.stack_list = []

#Stack: Push for Stack That Uses List ( ** Interview Question)

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def push(self, value):
        self.stack_list.append(value)

#Stack: Pop for Stack That Uses List ( ** Interview Question)

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def pop(self):
        if not self.stack_list:
            return None
        return self.stack_list.pop()

#Stack: Reverse String ( ** Interview Question)

def reverse_string(string):
    stack = Stack()
    reversed_string = ""

    for char in string:
        stack.push(char)

    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

"""
Stack: Parentheses Balanced ( ** Interview Question)
"""

def parantheses_balanced(string):
    stack = Stack()

    for i in string:
        if i == "(":
            stack.push(i)
        elif i == ")":
            if stack.is_empty() or stack.pop() !="(":
                return False
    return stack.is_empty()


"""
sort a stack 
"""
def sort_stack(stack):

    new_stack = Stack()

    while not stack.is_empty():

        temp = stack.pop()

        while not new_stack.is_empty() and new_stack.peek() > temp:
            stack.push(new_stack.pop())

        new_stack.push(temp)

    while not new_stack.is_empty():
        stack.push(new_stack.pop())