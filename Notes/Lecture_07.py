from math import floor, sqrt

# ITERATIVE
def fact_iter(n):
    total,k = 1,1 
    while k <= n:
        total,k = total*k, k+1
    return total

# RECURSIVE
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


# ORDER OF RECURSIVE CALLS
# --- Cascade

# First Implementation of Cascade
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


# Second Implementation of Cascade
def cascade_upd(n):
    """
    >>> cascade_upd(123)
    123
    12
    1
    12
    123
    >>> cascade_upd(1)
    1
    >>> cascade_upd(55)
    55
    5
    55
    """
    print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)

# FIBONACCI

# --- Fibonacci Sequence

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


def fib(n): # a tree-recursive process
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

# Fibonacci Call Tree

# Broken Fibonacci
#... This will print Recursion Error. fib(-10 and so on never computed.
#... There is going to be a limit for recursion, you might want to change.

def broken_fib(n):
    if n == 0:
        return 0
    # Missing Base Case
    else:
        return broken_fib(n-2) + broken_fib(n-1)

# Counting Partitions
""" How many different ways can I give out 
6 pieces of chocolate if nobody can have more than 4 pieces?

Largest Piece:4
2 + 4 = 6
1 + 1 + 4 = 6 

Largest Piece:3
3 + 3 = 6
1 + 2 + 3 =6
1 + 1 + 1 + 3 = 6

Largest Piece:2
2 + 2 + 2 = 6
1 + 1 + 2 + 2 = 6
1 + 1 + 1 + 1 + 2 = 6

Largest Piece:1
1 + 1 + 1 + 1 + 1 + 1 = 6
"""
"""
>>> count_piece(6,4)
9
"""

# Counting Partitions                                                                              
#......Ideas
#.........Find simpler instances of the problem
#.........Explore two possibilities:
#.............Use a 4
#.............Don't use a 4
#.........Solve two simpler problems:
#.............count_part(2,4)
#.............count_part(6,3)
#.........Sum up the results of these smaller problems!
 
def count_part(n , m) :
    if n == 0:
        return 1
    elif n < 0: 
        return 1
    elif m == 0:
        return 0 
    else:
        with_m : count_part(n - m, m)
        wo_m : count_part(n, m - 1)
        return with_m + wo_m
