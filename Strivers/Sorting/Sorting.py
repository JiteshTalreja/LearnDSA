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


print(selection_sort([5,6,4,7,2,1,3]))