"""
Merge sort is an efficient, stable, divide-and-conquer sorting algorithm that sorts a list by recursively splitting it into halves until each sublist contains a single element.
These single-element lists are then merged in sorted order, creating larger sorted subarrays until the entire list is combined. It is known for its consistent
O(nlogn) time complexity.

"""


def merge(l1, l2):
    l3= []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i+=1
        else:
            l3.append(l2[j])
            j+=1
    while i < len(l1):
        l3.append(l1[i])
        i+=1
    while j < len(l2):
        l3.append(l2[j])
        j+=1
    return l3


def merge_sort(my_list):

    if len(my_list)==1:
        return my_list

    mid = int(len(my_list)/2)
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    return merge(left, right)

print(merge_sort([1,3,7,8,2,4,5,6,9]))