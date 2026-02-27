"""
Queue Using Stacks: Enqueue ( ** Interview Question)
You are given a class MyQueue that implements a queue using two stacks.

Your task is to implement the enqueue method that should add an element to the back of the queue.

To achieve this, you can use the two stacks stack1 and stack2.

Initially, all elements are stored in stack1 and stack2 is empty.

To add an element to the back of the queue, you need to first transfer all elements from stack1 to stack2 using a loop that pops each element from stack1 and pushes it onto stack2.

Once all elements have been transferred to stack2, push the new element onto stack1. Finally, transfer all elements from stack2 back to stack1 in the same way as before, so that the queue maintains its ordering.

Your implementation should satisfy the following constraints:



The method signature should be def enqueue(self, value).

The method should add the element value to the back of the queue.



NOTE: I have added some diagrams under the Hints tab that show how this works, step-by-step.

"""


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(value)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0


    def dequeue(self):
        if self.stack1:
            temp = self.stack1.pop()
            return temp
        return None