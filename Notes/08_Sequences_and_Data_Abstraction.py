from math import floor, sqrt

############ SEQUENCES & DATA ABSTRACTION ################

'''
Complete the Homework 1 & 2
'''

# SEQUENCES...............................................
''' A sequence is an ordered collection of values.

strings
values

'''

# SEQUENCE ABSTRACTION

'''
All sequences have finite length.
Each element in a sequence has a  discrete integer indey.

Sequences share common behaviors based on the shared trait of having a
finite length and indexed elements.
  .Retrieve an element in a particular position
  .Create a copy of a subsequence
  .Check for membership
  .Concatenate two sequences together.

'''

# What can you do with sequences?
'''
Get Item
Check membership
Slice a subsequence
Concatenate
'''

# Iterating through Sequences

lst = [1,2,3,4,5]
i = 0
while i < len(lst):
    print(i, ':', lst[i])
    i += 1


lst = [1,2,3,4,5]
for elem in lst:
    print(elem)

''' These two definitions are functionally equivelant'''

# Range

'''
The range functon creates a sequence containing the values within a specifed
range.
            range(<start>, <end>, <skip>)

Creates a range object from <start> (inclusive) to <end> (exclusive), skipping
every <skip> element.
'''

for e in range(1, 8, 2):
    print(e)

    lst = [8,9,10]
    for i in range (len(lst)):
        print(i, ":", lst[i])

# List Comprehensions

'''
You can create out of a sequence using a list Comprehension:

                    [<exp> for <name> in <seq> if <cond>]

lst = []
for <name> in <seq>:
    if <cond>:
        lst += [<expr>]


Rules for Execution
1) Create an empty result list that will be the value of the list
comprehension
2) For each element in <seq>:
    A. Bind to that element to <name>
    B. If <cond> evaluates to a true value,
        then add the value of <exp> to the result list

Note: binding to <name> will not overwrite local bindings
'''

lst = []
for i in range(10):
    lst = lst + [i]
lst
[x for x in range(10)]

[x for x in range(10) if x % 2 == 0]

lst = []

for x in range(10):
    lst = lst + [x]

x

[x for x in range(10)]
[y for y in range(10)]
''' y is not defined '''


[x*2 for x in range(10) if x % 2 == 0]

# List Comprehension Examples

[x**2 for x in [1,2,3]]

[c + "0" for c in "cs61a"]

[e for e in "skate" if e>"m"]

[[e+1] for e in [1,2,3]]

[x for x in range(0,10) if x % 2 == 0 or x ==3 ]


# DATA ABSTRACTION.......................................

'''
/Compound values combine other values together
    A date: a year, a month, and a day
    A geographic position: latitude and longitude
/Data abstraction lets us manipulate compound values as units
/Isolate two parts of any program that uses data:
    - How data are represented (as parts)
    - How data are manipulated (as units)
/Data abstraction: A methodology by which functions enforce an abstraction
barrier between representation and use
'''

# Rational Numbers

'''
Numerator / Denominator

Exact representation as fractions
A pair of integers
As soon as division occurs, the exact representation may be lost!
Assume we can compose and decompose rational numbers:

    #Constructor    - rational (n,d) returns a rational number
    #Selectors      - numer(x) returns the Numerator of x
    #Selector       - denom(x) returns the Denominator of x

'''

1/3
1/3 == 0.33333333333333333333333333333333312345678
0.33333333333333333333333333333333312345678

# Rational Number Arithmetic

x = rational(1,4)
y = rational(5,8)
z = mul_rational(x,y)


'''
These functions implement an abstract representation for rational Numbers
        | 
        v
rational(n,d) returns a rational number x
numer(x) returns the Numerator of x
denom(x) returns the Denominator of x
'''



def mul_rational(x,y):
    return rational(numer(x) * numer(y),denom(x)*denom(y))

def add_rational(x,y):
    '''The sum of rational numbers X and Y'''
    nx,dx = numer(x), denom(x)
    ny,dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def nul_rational(x,y):
    '''The product of rational numbers X and Y'''
    return rational(mumer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
    '''Print rational X.'''
    print(numer(x), '/', denom(x))

def rationals_are_equal(x):
    '''True if rational numbers X and Y are equal'''
    return numer (x) * denom(y) == numer (y) * denom(x)

# Representing Rational Numbers

# Constructors and Selectors

from fractions import gcd

def rational(n,d):
    """A representation of the rational number N/D"""
    b = gcd(n,d)
    def select(a):
        if a == 'n':
            return n // b
        elif a == 'd':
            return d // b
    return select    #Construct a list

def numer(x):
    """Return the Numerator of rational number x"""
    return x('n')

def denom(x):
    """Return the Denominator of rational number x"""
    return x('d') #Select item from a list


## Reducing to Lowest Terms

'''
from fractions import fcd (Greatest Common Divisor)
def

def rational(n,d):
    """A representation of the rational number N/D"""
    a = gcd(n,d) # Always has the sign of d
    return [n // a, d // g]

'''

# Abstraction Barriers

'''
Parts of the program that....
    Use rational number to perform computation
    ------------------------------------------
    Create rationals or implement rational operators  ===== |
    ------------------------------------------              |
    Implement selectors and Constructor for rationals       |
                                                            |
Treat rationals as...                                       |
    whole data values                                       |
    -------------------------------------------             | Implementation
    Numerators and Denominator                        ======|
    -------------------------------------------             |
    two-element lists                                       | of
                                                            |
Using ...                                                   |
add_rational                                                | Lists
    mul_rational                                            |
    rationals_are_equal                                     |
    print_rational                                          |
    --------------------------------------------            |
    rational, numer, denom                          ======= |
    -------------------------------------------
    list literals and element selection

'''

# Violating Abstraction Barriers

add_rational([1,2],[1,4])
#               |    |
#   Does not use Constructors

def divide_rational(x,y):
    return [x[0] * y[1], x[1] * y[0]]
#           |
#       No Selectors
#       |                           |
#        ___________________________
#                   |
#                 And no constructors
