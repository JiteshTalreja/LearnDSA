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



def bubble_sort(nums):
    for i  in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
        
    return nums

print('bubble: ', bubble_sort([5,6,4,7,2,1,3]))


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