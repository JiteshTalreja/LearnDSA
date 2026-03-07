""" Q1
HT: Item In Common ( ** Interview Question)
Write a function item_in_common(list1, list2) that takes two lists as input and returns True if there is at least one common item between the two lists, False otherwise.

Use a dictionary to solve the problem that creates an O(n) time complexity.
"""


def item_in_common(list1, list2):
    dict1 = {}

    for i in list1:
        dict1[i] = True

    for j in list2:
        if j in dict1:
            return True
    return False


""" Q2
HT: Find Duplicates ( ** Interview Question)
find_duplicates()


Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).


Input:

A list of integers nums.


Output:

A list of integers representing the numbers in the input array nums that appear more than once. If no duplicates are found in the input array, return an empty list [].



Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
Output: [2, 3]
Explanation: The numbers 2 and 3 appear more than once in the input array.
"""

def find_dups(nums):
    dict1 = {}
    dups = []

    for i in nums:
        dict1[i] = dict1.get(i, 0) + 1
    
    for j in dict1:
        if dict1[j] > 1:
            dups.append(j)
    return dups


""" Q3
HT: First Non-Repeating Character ( ** Interview Question)
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). 
If there is no non-repeating character in the string, the function should return None.

For example, if the input string is "leetcode", the function should return "l" because "l" is the first character that appears only once in the string. 
Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating character in the string.
"""

def first_non_repeating_char(string):

    dict1 = {}

    for i in string:
        dict1[i] = dict1.get(i, 0) + 1

    for j in dict1:
        if dict1[j] == 1:
            return j
    return None

""" Q4
HT: Group Anagrams ( ** Interview Question)
You have been given an array of strings, where each string may contain only lowercase English letters. 
You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). 
The function should return a list of lists, where each inner list contains a group of anagrams.

For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], the function should return [["eat","tea","ate"],["tan","nat"],["bat"]] 
because the first three strings are anagrams of each other, the next two strings are anagrams of each other, and the last string has no anagrams in the input array.
"""

def group_anagrams(arr):
    dict1 = {}

    for i in arr:
        key = "".join(sorted(i))
        if key not in dict1:
            dict1[key] = []

        dict1.key.append(i)
    return dict1


""" Q5
HT: Two Sum ( ** Interview Question)
two_sum()

Problem:
Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

The main challenge here is to implement this function in one pass through the array. This means you should not iterate over the array more than once. 
Therefore, your solution should have a time complexity of O(n), where n is the number of elements in nums.

Input:
A list of integers nums .
A target integer target.

Output:
A list of two integers representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list [].
Example:

Input: nums = [5, 1, 7, 2, 9, 3], target = 10
Output: [1, 4]
Explanation: The numbers at indices 1 and 4 in the array add up to the target 10.
 
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: The numbers at indices 1 and 2 in the array add up to the target 6.
 
Input: nums = [3, 3], target = 6
Output: [0, 1]
Explanation: The numbers at indices 0 and 1 in the array add up to the target 6.
 
Input: nums = [2, 1, 2, 7, 11, 15], target = 9
Output: [2, 3]
Explanation: Notice there are two 2s in the array.  The second one will be used.
 
Input: nums = [1, 2, 3, 4, 5], target = 10
Output: []
Explanation: There are no two numbers in the array add up to the target 10.
 
Input: nums = [], target = 0
Output: []
Explanation: There are no numbers in the input array, so the function returns an empty list [].
"""

def two_sum(nums, target):
    dict1= {}

    for i, v in enumerate(nums):

        compliment = target - v
        if compliment in dict1:
            return [dict1[compliment], i]
        dict1[v] = i

    return []

""" Q6
HT: Subarray Sum ( ** Interview Question)
Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

Your function should take two arguments:

nums: a list of integers representing the input array

target: an integer representing the target sum


Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.

For example:
nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))  # should print [1, 3]


Note that there may be multiple subarrays that add up to the target sum, but your function only needs to return the indices of any one such subarray. Also, the input list may contain both positive and negative integers.
"""


def subarray_sum(nums, target):
    dict1 = {0: -1}
    current_sum = 0

    for i, v in enumerate(nums):
        current_sum += v

        if current_sum - target in dict1:
            return [dict1[current_sum - target] + 1, i]

        dict1[current_sum] = i

    return []