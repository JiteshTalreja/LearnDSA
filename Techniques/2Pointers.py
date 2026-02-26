"""

## Q1 Reverse Vowels from a Given String
ex:
input : 'hello'
output : 'holle'
"""

def reverse_vowels(string):

    vowels = 'aeiouAEIOU'
    lstring = list(string)
    n = len(lstring)
    i = 0
    j = n-1

    while i < j:
        if lstring[i] not in vowels:
            i +=1
        elif lstring[j] not in vowels:
            j -=1
        else:
            lstring[i], lstring[j] = lstring[j], lstring[i]
            i +=1
            j-=1
    return ''.join(lstring)


"""
## Q2 Remove duplicates from a sorted list in O(1) space and O(n) time complexity

"""

def remove_dups(arr):

    i = 0
    j = 1

    while j < len(arr):
        if arr[i] == arr[j]:
            j +=1
        else:
            i +=1
            arr[i] = arr[j]
            j+=1
    return arr[:i+1]

"""
## Q3 Reverse words in a sentence:
ex: 
input: 'this is a sentence'
output: 'sentence a is this'

"""


def reverse_sentence(sen):
    list_sen = list(sen[::-1])

    n = len(list_sen)
    i = 0
    r = 0
    l = 0

    while i < n:
        while i < n and list_sen[i] != ' ':
            list_sen[r] = list_sen[i]
            r += 1
            i += 1

        if l < r:
            list_sen[l:r] = list_sen[l:r][::-1]
            if r < n:
                list_sen[r] = ' '
                r += 1
            l = r
        i += 1
    return ''.join(list_sen[:r])