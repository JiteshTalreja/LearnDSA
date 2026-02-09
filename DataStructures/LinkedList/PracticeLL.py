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