"""
Q1 Print name 5 time
"""

def print_name(name, n, count):
    if count >= n:
        return
    print(name)
    print_name(name, n, count+1)

"""
Q2 print from 1 to N
"""

def print_1_to_n(n):
    if n <=0:
        return
    print_1_to_n(n-1)
    print(n)


"""
Q3 print N to 1
"""

def print_n_to_1(n):

    if n <= 0:
        return
    print(n)
    print_n_to_1(n-1)
print_n_to_1(10)