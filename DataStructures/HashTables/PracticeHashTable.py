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
