from DoublyLinkedList import Node
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


def reverse2(self, x):
    temp = self.head
    while temp is not None:
        # swap the prev and next pointers of node points to
        temp.prev, temp.next = temp.next, temp.prev

        # move to the next node
        temp = temp.prev

    # swap the head and tail pointers
    self.head, self.tail = self.tail, self.head


## PARTITION LIST (EDGE CASE WHERE 1 LL IS EMPTY
def partition_list(self, x):
        if self.head is None:
            return None

        dummy1 = Node(0)
        dummy2 = Node(0)

        prev1 = dummy1
        prev2 = dummy2

        current = self.head

        while current:
            if current.value < x:
                prev1.next = current
                current.prev = prev1
                prev1 = current
            else:
                prev2.next = current
                current.prev = prev2
                prev2 = current

            current = current.next

        prev1.next = dummy2.next
        if dummy2.next:
            dummy2.next.prev = prev1
        prev2.next = None
        self.head = dummy1.next
        self.head.prev = None


## REVERSE BETWEEN

def reverse_between(self, start_index, end_index):
    if self.length <= 1 or start_index == end_index:
        return

    dummy = Node(0)
    dummy.next = self.head
    self.head.prev = dummy

    prev = dummy
    for _ in range(start_index):
        prev = prev.next

    current = prev.next

    for _ in range(end_index - start_index):
        node_to_move = current.next

        current.next = node_to_move.next
        if node_to_move.next:
            node_to_move.next.prev = current

        node_to_move.next = prev.next
        prev.next.prev = node_to_move
        prev.next = node_to_move
        node_to_move.prev = prev

    self.head = dummy.next
    self.head.prev = None


## SAWP NODES IN PAIRS

def swap_pairs(self):
    dummy_node = Node(0)
    dummy_node.next = self.head
    previous_node = dummy_node

    while self.head and self.head.next:
        first_node = self.head
        second_node = self.head.next

        previous_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        second_node.prev = previous_node
        first_node.prev = second_node

        if first_node.next:
            first_node.next.prev = first_node

        self.head = first_node.next
        previous_node = first_node

    self.head = dummy_node.next

    if self.head:
        self.head.prev = None