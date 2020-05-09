#######################################
##    MUTABLE FUNCTIONS & GROWTH     ##
#######################################
#        by  Chris Allsman

# Functions with Behavior That Changes Ove Time ...............................

def square(x):
    return x*x

'''
>>> square(5) # Returns the same value when called with the same input
25
>>> square(5)
25
>>> square(5)
25
>>>
'''

'''
>>> def f(x):
... ... ...

>>> f(5)            ====> Return values are different when called with the
25                        same input
>>> f(5)
26
>>> f(5)
27
'''

'''
EXAMPLE
    Let's model a bank account that has a balance of $100

>>> withdraw(25) =====> Argument: amount to withdraw              <=====|
75               =====> Return Value: Remaining balance                 |
                                                                        |
>>> withdraw(25) =====> Second withdrawal of the same amount            |
50               =====> different return value                          |
                                                                        |
>>> withdraw(60)                                                        |
'Insufficient funds'  => Where's this balance stored?                   |
>>> withdraw(15)                                                        |
35                                                                      |
>>> withdraw = make_withdraw(100) ==> Within the parent frame of the function
        A function has a body and a parent environment
'''

# Non-Local Assignment & Persistent Locak State ................................

'''Try it in Python Tutor'''

def make_withdraw(balance):
    ''' Return a withdraw function with a starting balance'''
    def withdraw(amount):
        nonlocal balance     # ------> declare the name 'balance' nonlocak at the top of
        if amount > balance: #         the bosy of the function in which it is re-assigned.
            return 'Insufficient funds'
        balance = balance - amount # Re-bind balance in the first non-locak frame in
        return balance             # which it was bound previously
    return withdraw

# withdraw = make_withdraw(100)
# withdraw(25)
# withdraw(25)
# withdraw(60)
# withdraw(15)


# The Effect of Nonlocal Statements ..........................................

'''                 nonlocal <name>
Effect: Future assignments to that name change its pre-existing binding in the
'first non-local frame' of the 'current environment' in which that name is bound.
                                    ^
                                    |
                                    |
                             Python Docs: an 'enclosing scope'

From the Python 3 language reference:

Names listed in a nonlocal statement must refer to pre-existing bindings in an
enclosing scope.
Names listed in a nonlocal statement must not collide with pre-existing bindings
in the local scope.
""'''

# The Many Meanings of Assignment Statements ................................
'''
--------------------------------------------------------------------------------
x = 2
--------------------------------------------------------------------------------
        STATUS                  |                  EFFECT
--------------------------------|-----------------------------------------------
 . No nonlocal statement        | Create a new binding from name 'x' to object 2
 . 'x' is not bound locally     | in the first frame of the current environment
--------------------------------|-----------------------------------------------
. No nonlocal statement         | Re-bind name 'x' to object 2 in the first frame
. 'x' is bound locally          | of the current environment
--------------------------------|-----------------------------------------------
. nonlocal x                    | Re-bind 'x' to 2 in the first non-local frame
. 'x' is bound in a non-local   | of the current environment in which 'x' is
frame                           | bounded
--------------------------------|-----------------------------------------------
. nonlocal x                    | SyntaxError: no bindings for nonlocal 'x' found
. 'x' is not bound in a         |
non-local frame                 |
--------------------------------|-----------------------------------------------
. nonlocal x                    | SyntaxError: name 'x' is parameter and nonlocal
. 'x' is bound in a non-local   |
frame                           |
. 'x' is also bound locally     |
--------------------------------------------------------------------------------
'''

# Python Particulars ..........................................................
'''
PYthon pre-computeswhich frame contains each name before executing the body of
a function.
Within the body of a function, all instances of a name must refer to the same
name.
'''

'''
>>> def make_withdraw(balance):
...     def withdraw(amount):
...         if amount > balance:
...             return 'Insufficient funds'
...         balance = balance - amount    # Locak Assignment
...         return balance
...     return withdraw
...
>>> wd = make_withdraw(20)
>>> wd(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in withdraw
UnboundLocalError: local variable 'balance' referenced before assignment
'''

''' Two different functions
>>> chris = make_withdraw(100)
>>> john = make_withdraw(100000)
>>> chris
<function make_withdraw.<locals>.withdraw at 0x105594f28>
>>> john
<function make_withdraw.<locals>.withdraw at 0x1055b9048>
>>> chris == john
False
>>> chris is john
False
>>> chris(10)
90
>>> chris(10)
80
>>> john(1000)
99000
>>> chris(10)
70
>>> john(1000)
98000
>>> chris(1000)
'Insufficient funds'
>>> chris(10)
60
>>> chris(1)
59
>>> chris(1)
58
>>> chris(1)
57
>>> chris(17)
40
>>> john(10000)
88000
>>> john(80000)
8000
>>> john(7950)
50
>>> john(10)
40
>>> chris != john
True
>>> chris is not john
True
>>> chris(0) == john(0)
True
>>> chris(0)
40
>>> john(0)
40
>>>
'''

# Mutable Values & Persistent Local State .....................................

'''
Mutable values can be change without a nonlocal statement.
'''


def make_withdraw_list(balance):
    b = [balance]       # Name bound outside of withdraw def
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount    # Element assignment changes a list
        return b[0]
    return withdraw

wd = make_withdraw_list(100)
wd(25)

# Referential Transparency, Lost ..............................................

'''
Expressions are referentially transparent if substituting an expression with its
value does not change the meaning of a program
            mul(add(2,mul(4,6)),add(3,5))
            mul(add(2,  24    ),add(3,5))
            mul(      26       ,add(3,5))

Mutation operations violate the condition of referential transparency beacuse they
do more than just return a value; 'they change the environment'.
'''

''' EXAMPLE #Try in Python Tutor'''
def f(X):
    x = 4
    def g(y):
            def h(z):
                    nonlocal x
                    x = x + 1
                    return x + y + z
            return h
    return g
a = f(1)
b = a(2)
total = b(3) + b(4)

# Summary (AKA What do I need to know for the MT) ..............................
'''
. Nonlocal allows you to modify a binding in a parent frame, instead of just
looking it up
. Don't need a nonlocal statement to mutate a value
. A variable declared nonlocal must:
    .Exist in a parent frame (other than the global frame)
    .Not exist in the current frame
'''

#######################################
##         PROGRAM PERFORMANCE       ##
#######################################

# Measuring Growth ............................................................
'''
. Different functions run in different amounts of time
    . Different implementations of the same program can also run in different
    amounts of time
. How do we measure this?
    . Amount of time taken to run once?
    . Average time taken to run?
    . Average across a bunch of different computers?
    . Number of operations?
'''

''' EXAMPLE GROWTH'''

total = 0

def count(f):
    def counted_f(*args):
        global total
        total += 1
        return f(*args)
    return counted_f

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib_iter(n):
    global total
    curr, nxt, i = 0, 1, 0
    while i < n:
        curr, nxt = nxt, curr + nxt
        i += 1
        total += 1
    return curr

memo = {}

def memoized_fib(n):
    if n in memo:
        ans = memo[n]
    elif n <= 2:
        ans = 1
        memo[n] = ans
    else:
        ans = memoized_fib(n-2) + memoized_fib(n-1)
        memo[n] = ans
    return ans
'''
>>> total = 0
>>> fib_iter(30)
832040
>>> total
30
>>> total = 0
>>> memoized_fib = count(memoized_fib)
>>> memoized_fib(30)
832040
>>> total
2
>>> total = 0
>>> memoized_fib(100)
354224848179261915075
>>> total
282
>>> fib(100)
^CTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "12.py", line 290, in fib
    return fib(n-1) + fib(n-2)
  File "12.py", line 290, in fib
    return fib(n-1) + fib(n-2)
  File "12.py", line 290, in fib
    return fib(n-1) + fib(n-2)
  [Previous line repeated 86 more times]
  File "12.py", line 288, in fib
    if n == 1:
KeyboardInterrupt
'''

# Improving Number of Operations .............................................
'''
. Getting better performance usually requires clever thought
    . Some tools can be used to speed up performance (Ex: memoization, up next)
    . Other times, need to have a different approach or incorporate some insight
'''

''' Iterative Solution
def fib(n):
    curr, next, i = 0, 1, 0
    while i < n:
        curr, next = next, curr + next
        i += 1
    return curr
'''

"""Recursive Call
def fib(n):
    if n < 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
"""

# Improving Fib with Memoization ..............................................
#                           fib(5)
#                       /              \
#                  fib(3)             fib(4)
#             /            \         /            \
#       fib(1)          fib(2)     fib(2)         fib(3)
#          |        /        \     /     \        /      \
#         1       fib(0)  fib(1)  /       \      /        \
#                  |         |  fib(0)   fib(1) fib(1)     fib(2)
#                  0         1   |          |     |       /      \
#                                0          1     1    fib(0)    fib(1)
#                                                         |        |
#                                                         0        1


# Basic Idea to Improve
'''
Basic idea for improving fibonacci is once I compute a value, I store for future
use.
'''

# def better_fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif already called better_fib(n): # Use a container to store these values!
#         return stored value
#     else:
#         store & return better_fib(n-2) + better_fib(n-1)

''' Standart Recursive Call vs Stored Recursive Call Performance

'''

#######################################
##            COUNTING               ##
#######################################

# How to count calls ..........................................................

'''
Can't always rely on having a program to count calls.
    . For an iterative function: step through the program, and identify how many
    times you need to go through the loop before exiting
    . For Recursive function: draw out an environment diagram/call tree

After you do this for a few example inputs, you can find patterns to estimate the
number of steps for other inputs.
'''

# 'Patterns' of Growth .........................................................

'''
There are common patterns for how functions grow.
Because these patterns often aren't linear, you often can't use just one input
to compare programs.
Instead, you have to identify the overall pattern.
'''

# Some quick notation ........................................................

'''
'a', 'b' and 'k' usually refer to constants (do not depend on any particular
function call)

'x' and 'n' refer to variables dependent on the input to the function (change
with each function call)

So x^b represents x^2, x^4, etc.
'''

# Common Patterns (I) .........................................................

'''
Constant Growth                          Linear Growth
    # Operations the same regardless      Increasing input by 1 adds a constant
    of the imput size.                    amount to # of operations

    Grows like: k                         Grows like: ax + b

'''
# Common Patterns (I) .........................................................
'''
Logarithmic Growth                        Exponential Growth
    # operations grows only when input     Increasing input by 1 doubles (or
    is multiplied (doubled,tripled, etc)   triples, quadruples, etc.) # operations

    Grows like: logb(x)                    Grows like: k^x (2^x, 3^x, etc.)
'''

# Summary (AKA what do I need to know) .........................................


'''
There are different methods of programmatically or manually counting the Number
of operations for a function
    . You should be able to do this for small inputs
There are 4 main 'patterns' of growth which we can apply to sets of data.
    . Given the number of operations for a set of inputs, should be able to
    identify these
'''

# What you don't need to know? .................................................
'''
Formal notation of describing growh
    . Ex. O(2^n)

identifying growth classes just by looking at code.
'''
