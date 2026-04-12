"""
1. Two Sum
"""

def twosum(nums, target):
    dict1 = {}

    for i, v in enumerate(nums):

        res_number = target - v

        if res_number in dict1:
            return [dict1[res_number], i]

        dict1[v] = i


"""
20. Valid Parenthesis
"""

def isValid(self, s: str) -> bool:
    stack = []
    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:
        if ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return len(stack) == 0