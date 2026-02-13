from logging import setLogRecordFactory
from threading import current_thread

from DataStructures.LinkedList.LinkedList import Node

# Find middle of the linked list

def find_middle_node(self):
    if self.head is None:
        return None
    fast = slow = self.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


# find is the llinked list has loop

def has_loop(self):
    slow = self.head
    fast = self.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False



## find kth node in the ll from the end:

def find_kth_from_end(ll, k):
    slow = fast = ll.head

    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    return slow

## Remove duplicates from a linked list

## O(n2) using 2 while loops
def remove_duplicates(self):
    current = self.head

    while current:

        runner = current
        while runner.next:

            if runner.next.value == current.value:
                runner.next = runner.next.next
                self.length -= 1
            else:
                runner = runner.next
        current = current.next

## Using set
def remove_duplicates_set(self):
    values = set()
    current = self.head
    previous = None
    while current:
        if current.value in values:
            previous.next = current.next
            self.length -=1
        else:
            values.add(current.value)
            previous = current
            current = current.next

## Remove duplicates from a python list
def remove_duplicates1(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2
print(remove_duplicates1([1,2,3,1,4,5,2]))


def remove_duplicates_again(ll):
    current = ll.head

    while current:
        runner = current

        while runner.next:
            if current.value == runner.next.value:
                runner.next = runner.next.next
                ll.length -=1
            else:
                runner = runner.net
        current = current.nexxt

def remove_duplicates_set_again(ll):
    values = set()
    current = ll.head
    previous = None

    while current:

        if current.value in values:
            previous.next = current.next
            ll.length -= 1
        else:
            values.add(current.value)
            previous = current
            current = current.next


def binary_to_decimal(ll):
    current = ll.head
    dec = 0

    while current:
        dec = dec * 2 + current.value
        current = current.next
    return dec

def partition(ll, x):
    if ll.head is None:
        return None

    dummy1 = Node(0)
    dummy2  = Node(0)

    prev1 = dummy1
    prev2 = dummy2

    current = ll.head

    while current:
        if current.value < x:
            prev1.next = current
            prev1 = current
        else:
            prev2.next = current
            prev2 = current
        current = current.next
    prev1.next = dummy2.next
    prev2.next = None
    ll.head = dummy1.next


def rotate_right_with_k(ll, k: int):
    head = ll.head
    if not head or not head.next or k == 0:
        return head

    # Step 1: Find length
    length = 1
    tail = head

    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Reduce k
    k = k % length
    if k == 0:
        return head

    # Step 3: Make circular
    tail.next = head

    # Step 4: Find new tail
    steps_to_new_tail = length - k
    new_tail = head

    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    # Step 5: Set new head
    new_head = new_tail.next

    # Break the circle
    new_tail.next = None

    return new_head

def reverse_between(self, start_index, end_index):
    if self.length <= 1:
        return

    dummy_node = Node(0)
    dummy_node.next = self.head
    previous_node = dummy_node

    for i in range(start_index):
        previous_node = previous_node.next

    current_node = previous_node.next

    for i in range(end_index - start_index):
        node_to_move = current_node.next
        current_node.next = node_to_move.next
        node_to_move.next = previous_node.next
        previous_node.next = node_to_move

    self.head = dummy_node.next

def reverse_between_2(ll, x, y):
    if ll.length <=1:
        return


    dummy = Node(0)
    dummy.next = ll.head
    prev = dummy

    for _ in range(x):
        prev = prev.next

    current=  prev.next

    for _ in range(y - x):
        to_move = current.next

        current.next = to_move.next
        to_move.next = prev.next
        prev.next = to_move
    ll.head = dummy.next
    return ll.head