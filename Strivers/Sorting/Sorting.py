##Selection sort

"""in selection sort we select the minimum and pull it in the front of the array ( or pull it at the very start of array)"""


def selection_sort(nums):

    for i in range(len(nums)):

        min_idx = i

        for j in range(i, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[min_idx], nums[i] = nums[i], nums[min_idx]
    return nums


print('selection: ', selection_sort([5,6,4,7,2,1,3]))

## BUBBLE SORT

def bubble_sort(nums):
    for i  in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
        
    return nums

print('bubble: ', bubble_sort([5,6,4,7,2,1,3]))

##INSERTION SORT

def insertion_sort(nums):

    for i in range(1, len(nums)):
        key = nums[i]

        j = i-1

        while j >=0 and nums[j] > key:
            nums[j+1] = nums[j]
            nums[j] = key
            j-=1
    return nums


print('insertion: ', insertion_sort([5,6, 4, 7, 2, 3, 1]))


## MERGE SORT

def merge(l1, l2):
    i = 0
    j = 0
    l3 = []

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
    while j< len(l2):
        l3.append(l2[j])
        j+=1
    return l3

def merge_sort(nums):

    if len(nums) == 1:
        return nums

    mid = int(len(nums)/2)

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

print(merge_sort([1,3,7,8,2,4,1, 2, 5,6,9]))