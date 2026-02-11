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
        ll.head = dummy1.next
        prev2.next = None