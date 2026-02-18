## Palindrome checker
from ctypes.util import dllist


## MY SOLUTION
def is_palindrome(self):
    if self.length <= 1:
        return True
    forward = self.head
    backward = self.tail
    for _ in range(self.length // 2):
        if forward.value == backward.value:
            forward = forward.next
            backward = backward.prev
        else:
            return False
    return True

## Course Solution
def is_palindrome_course(self):
    if self.length <= 1:
        return True
    forward_node = self.head
    backward_node = self.tail
    for i in range(self.length // 2):
        if forward_node.value != backward_node.value:
            return False
        forward_node = forward_node.next
        backward_node = backward_node.prev
    return True


## REVERSE A DOUBLY LINKED LIST

## MY SOLUTION
def reverse(self):

    current = self.head
    prev = None

    self.head = self.tail
    self.tail = current

    while current:
        current.prev = current.next
        current.next = prev
        prev = current
        current = current.prev


## COURSE SOLUTION

##Solution  # 1:


def reverse1(self):
    if not self.head or not self.head.next:
        return

    current = self.head
    temp = None

    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev

    temp = self.head
    self.head = self.tail
    self.tail = temp


##Solution  # 2


def reverse2(self):
    temp = self.head
    while temp is not None:
        # swap the prev and next pointers of node points to
        temp.prev, temp.next = temp.next, temp.prev

        # move to the next node
        temp = temp.prev

    # swap the head and tail pointers
    self.head, self.tail = self.tail, self.head