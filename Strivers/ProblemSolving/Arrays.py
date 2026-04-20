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


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q8 Find missing number in array

##Brute
def missing_brute(nums, n):

    for i in range(1, n):
        flag = False
        for j in range(0, n-1):
            if nums[j] == i:
                flag = True
                break
        if not flag:
            return i

print(missing_brute([1,2,4,5], 5))


## Better
def missing_better(nums, n):
    hash = [0]*(n+1)

    for i in nums:
        hash[i] = 1

    for i in range(1, n):
        if hash[i] == 0:
            return i

print(missing_better([1,2,4,5], 5))


## Optimal
def missing_optimal(nums, n):
    sum_n = int((n*(n+1))/2)
    cur_sum = 0
    for i in nums:
        cur_sum+=i

    return sum_n - cur_sum
print(missing_optimal([1,2,4,5], 5))

## Optimal 2
def missing_optimal2(nums, n):
    xor1 = 0
    xor2 = 0
    for i in range(0, n-1):
        xor1 ^= i+1
        xor2 ^= nums[i]
    xor1^=n
    return xor1^xor2

print(missing_optimal2([1,2,4,5,], 5))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q9 Find maximum consecutive 1s

def max_con_1(nums):
    maxi = 0
    counter = 0
    for i in nums:
        if i ==1:
            counter+=1
            maxi = max(maxi, counter)
        else:
            counter = 0
    return maxi
# print(max_con_1([1,1,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q9 Find the number that just appears once in an array

##Brute
def single_number_brute(nums):
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        if count == 1:
            return nums[i]

## Better
def single_number_better(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for num in nums:
        if freq[num] == 1:
            return num

## Optimal
def single_number_optimal(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
## Q10 Find Longest Subarray with Sum - k

##Brute

def long_brute(nums, k):
    n = len(nums)
    longest = 0

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                longest = max(longest, j - i + 1)
    return longest

print('long: ', long_brute([1,2,3,1,1,1,1,4,5,2], 3))

## Optimal (USING PrefixSum)
"""
In python since we are using dict this is O(n), for C++ Striver was using ordered map which has search complexity of Logn
"""


def longest_subarray_sum_k(nums, k):
    prefix_sum = 0
    max_len = 0
    mp = {}  # prefix_sum -> first index

    for i in range(len(nums)):
        prefix_sum += nums[i]

        # Case 1: subarray from 0 to i
        if prefix_sum == k:
            max_len = i + 1

        # Case 2: subarray in between
        if (prefix_sum - k) in mp:
            length = i - mp[prefix_sum - k]
            max_len = max(max_len, length)

        # Store only FIRST occurrence
        if prefix_sum not in mp:
            mp[prefix_sum] = i

    return max_len
print("long optimal:", longest_subarray_sum_k([1, 0, 2, 0, 1], 3))

