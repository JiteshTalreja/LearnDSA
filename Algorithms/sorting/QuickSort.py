""" GPT GENERATED"""


def quicksort(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)

        quicksort(nums, low, pivot_index - 1)
        quicksort(nums, pivot_index + 1, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low

    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[high] = nums[high], nums[i]
    return i

"""COURSE"""

def pivot(my_list, pivot_index, end_index):

    swap = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap+=1
            my_list[i], my_list[swap] = my_list[swap], my_list[i]

    my_list[pivot_index], my_list[swap] = my_list[swap], my_list[pivot_index]
    return swap

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)


print(quick_sort([4,6,1,7,3,2,5]))