## Binary search


def binary_search(arr, val):

    start  = 0
    end = len(arr)

    while start < end:

        mid = (start + end)//2

        if arr[mid] == val:
            return mid

        if arr[mid] < val:
            start = mid+1
        else:
            end = mid-1
    return mid

l1 = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(l1, 1))


## Selection sort
""" sorts the array with O(n^2) complexity
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):

        min = i

        for j in range(i+1, n):

            if arr[j] < arr[min]:

                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

l2 = [99,6, 8, 2, 0, 11, 5]

print(selection_sort(l2))

