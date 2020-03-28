#Required Questions
# Q1: Syllabus Quiz
'''Please fill out our Syllabus Quiz based off of our policies found on our
syllabus page.
'''

# Q2: A Plus Abs B ............................................................
'''
Fill in the blanks in the following function for adding a to the absolute value
of b, without calling abs. You may not modify any of the provided code other than
the two blanks.
'''

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return h(a, b)']
    """
    if b >= 0: # b is positive, a + b
        h = add # a function, NOT a function call
    else: # b is negative, a + abs(b), a -(-b) = a + b
        h = sub
    return h(a, b) # function call

'''
Use Ok to test your code:

python3 ok -q a_plus_abs_b
'''

# Q3: Two of Three
'''
Write a function that takes three positive numbers and returns the sum of the
squares of the two smallest numbers. Use only a single line for the body of the
function.
'''

def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return min(x*x+y*y,x*x+z*z, y*y+z*z)

'''
Hint: Consider using the max or min function:

>>> max(1, 2, 3)
3
>>> min(-1, -2, -3)
-3
Use Ok to test your code:

python3 ok -q two_of_three

'''

# Q4: Largest Factor .........................................................
'''
Write a function that takes an integer x that is greater than 1 and returns the
largest integer that is smaller than x and evenly divides x.
'''

def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    ''' NOTES
    Start an n-1. Try every number until you hit a factor.
    1. counter(can be an input)
    2. Stop condition in the while statement. Breaks out when False
    3. Decrement/increment our counter (get closer to stop condition)
    '''

    factor = n -1
    while factor >0:  # This will break when 0>0. We will actually never hit this assuming n>0
        if n % factor == 0: # If the number is prime, then factor equals = 1 and n % 1 == 0 :
            return factor
        factor -= 1


'''
Hint: To check if b evenly divides a, you can use the expression a % b == 0,
which can be read as, "the remainder of dividing a by b is 0."

Use Ok to test your code:

python3 ok -q largest_factor
Q5: If Function vs Statement
Let's try to write a function that does the same thing as an if statement.
'''

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

'''
Despite the doctests above, this function actually does not do the same thing as
an if statement in all cases. To prove this fact, write functions c, t, and f
such that with_if_statement prints the number 6, but with_if_function prints
both 5 and 6.
'''

def with_if_statement():
    """
    >>> result = with_if_statement()
    6
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    5
    6
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    return False

def t():
    print(5)

def f():
    print(6)

'''
Hint: If you are having a hard time identifying how an if statement and
if_function differ, consider the rules of evaluation for if statements and call
expressions.
Use Ok to test your code:

python3 ok -q with_if_statement
python3 ok -q with_if_function
'''

# Q6: Hailstone
'''
Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach,
poses the following mathematical puzzle.

Pick a positive integer x as the start.
If x is even, divide it by 2.
If x is odd, multiply it by 3 and add 1.
Continue this process until x is 1.
The number x will travel up and down but eventually end at 1 (at least for all
numbers that have ever been tried -- nobody has ever proved that the sequence
will terminate). Analogously, a hailstone travels up and down in the atmosphere
before eventually landing on earth.

Breaking News (or at least the closest thing to that in math). There has been a
recent development in the hailstone conjecture that shows that almost all numbers
will eventually get to 1 if you repeat this process. This isn't a complete proof
but a major breakthrough
This sequence of values of x is often called a Hailstone sequence. Write a
function that takes a single argument with formal parameter name x, prints out
the hailstone sequence starting at x, and returns the number of steps in the
sequence:
'''
def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    length = 1
    while x != 1:
        print(x)
        if x % 2 == 0:
            x = x // 2 # Integer division prevents "1.0" output
        else:
            x = x * 3 + 1
        length = length + 1
    print(x) # x is now 1
    return length

'''
Hailstone sequences can get quite long! Try 27. What's the longest you can find?

Use Ok to test your code:

python3 ok -q hailstone
'''
