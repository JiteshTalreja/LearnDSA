#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q1 Find the largest number in an unsorted Array


## solution Brute force to sort the array.

## Optimal solution is below

def largest(nums):

    maxi = nums[0]

    for i in nums:
        if i > maxi:
            maxi = i
    return maxi
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

## Q2 second largest in a unsorted array

## AGAIN Brute force is to sort the array

## BETTER

def slargest(nums):

    ## First find the largest
    largest = nums[0]

    for i in nums:
        if i > largest:
            largest = i
    slargest = -1

    for i in nums:
        if i > slargest and i != largest:
            slargest = i
    return slargest

# print(slargest([3,20,10,15,2]))

## OPTIMAL SOLUTION

def sslargest_opt(nums):

    largest = nums[0]
    slargest = -1

    for i in nums:
        if i > largest:
            slargest = largest
            largest = i

        elif i < largest and i > slargest:
            slargest = i

    return slargest

# print('slarge opt', sslargest_opt([3,20,10,15,2]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q3 Check if list is sorted

def is_sorted(nums):
    for i, v in enumerate(nums):
        if v> nums[i+1]:
            return False
    return True

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q4 Remove duplicates from an array

def remove_dups(nums):
    i = 0
    j =1

    while j < len(nums):
        if nums[i] != nums[j]:
            i+=1
            nums[i] = nums[j]
        j+=1
    return nums[:i+1]

# print(remove_dups([1,1,1,2,2,2,3,3,3,4,4,4]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------LEFT ROTATE-------------------------------------------------------------------------------------------------
## Q5 Rotate an array by k places
## Right rotate by k = Left rotate by (n - k)

def left_rotate(nums, k):
    return nums[k:] + nums[:k]

# print(left_rotate([1,2,3,4,5,6,7], 3))

# another method

def left_rotate2(nums, k):
    k%=len(nums)
    n = len(nums)
    l2 = []
    for i in range(k):
        l2.append(nums[i])

    for i in range(k, n):
        nums[i-k] = nums[i]

    for i in range(n-k, n):
        nums[i] = l2[i-(n-k)]
    return nums
print("left_rotate2", left_rotate2([1,2,3,4,5,6,7], 3))

## best and Optimal solution for this is using reverse:
## Reverse first k
## reverse last n-k
## reverse full list


#------------------------------------------------RIGHT ROTATE------------------------------------------------------------------------------------------------


def reverse(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        r-=1
        l+=1

def right_rotate(nums, k):
    k %= len(nums)

    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)
    return nums
print(right_rotate([1,2,3,4,5,6,7], 3))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q6 Move all zeros at the end of an array

list1  = [1,0,2,3,2,0,0,4,5,1]

## [1,2,0,3,2,0,0,4,5,1]

def push_back(nums, item=0):
    i = 0
    j = 1

    while j<=len(nums)-1:
        print(j)
        if nums[i]==item and nums[j]!=item:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j+=1
        elif nums[i] != item:
            i+=1
            j+=1
        else:
            j+=1

    return nums

print(push_back(list1))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q7 Union  of 2 arrays:

## Brute
def union(l1, l2):
    set1 = set()

    for i in l1:
        set1.add(i)
    for j in l2:
        set1.add(j)
    return set1

print(union([1,1,2,3,4,5,], [2,3,4,4,5,6]))

## OPTIMAL
def union_sorted(l1, l2):
    i = j = 0
    res = []

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            if not res or res[-1] != l1[i]:
                res.append(l1[i])
            i += 1
        else:
            if not res or res[-1] != l2[j]:
                res.append(l2[j])
            j += 1

    while i < len(l1):
        if not res or res[-1] != l1[i]:
            res.append(l1[i])
        i += 1

    while j < len(l2):
        if not res or res[-1] != l2[j]:
            res.append(l2[j])
        j += 1

    return res

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q7 Intersection of 2 arrays:

##BRUTE
def intersection_with_duplicates(l1, l2):
    res = []
    used = [False] * len(l2)

    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j] and not used[j]:
                res.append(l1[i])
                used[j] = True
                break

    return res

## OPTIMAL

def intersection_sorted(l1, l2):
    l1.sort()
    l2.sort()

    i = j = 0
    res = []

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            res.append(l1[i])
            i += 1
            j += 1

    return res