###########################
##  NAMES & FUNCTIONS    ##
###########################

# Expressions & Values .......................................................

'''
Expressions evaluate to values in the one or more steps

    Expression                              Value
   ==============                          =========
    'hello!'  --------------------------->  'hello!'
        7/2   --------------------------->   3.5
 add(1, max(2,3)) ----------------------->    4

'''

# Names .......................................................................

'''
>>> 5*2
10
>>> 5**2
25
>>> 5/2
2.5
>>> 5//2
2
>>> 109*5469*3
1788363
>>> -5//2
-3
>>> 2*3.141519*3958.8
24873.290834400002
>>> (4/3)*3.141519*3958.8*3958.8*3958.8
259877758406.7838
>>> radius = 3958.8
>>> radius
3958.8
>>> (4/3)*3.141519*(radius**3)
259877758406.7838
>>> from math import pi
>>> pi
3.141592653589793
>>> 2*pi*radius
24873.873994062546
>>> (4/3)*pi*(radius**3)
259883851296.82016
>>> circ = 2*radius*pi
>>> circ
24873.873994062546
>>> vol = (4/3)*pi*(radius**3)
>>> vol
259883851296.82016
>>> circ*6
149243.2439643753
>>> vol/2
129941925648.41008
>>> radius = 2106.1
>>> radius
2106.1
>>> circ
24873.873994062546
>>> vol
259883851296.82016
>>> circ, vol = 2*pi*radius, (4/3)*pi*(radius**3)
>>> circ
13233.016575450925
>>> vol
39131416921.9656
>>>

Values can be assigned to 'names' to make referring to them easier.
A name can only be bound to a single value.
One way to introduce a new name in a program is with an 'assignment statement'


            x    =   1  +   2   *   3   -   4   //  5
            |       |--------------------------------|
          Name              Expression

Statements affect the program, but do not evaluate to values.

>>> radius = 2
>>> radius = 3
>>> radius
3
>>> old_radius = radius
>>> old_radius
3
>>> radius = 4
>>> radius
4
>>> old_radius
3
'''

###########################
##      FUNCTIONS        ##
###########################

# Functions ...................................................................

'''
'Functions' allow us to abstract away entire expressions and sequences of
computation.
They take in some input (known as their 'arguments') and transform it into an
input ('the return value')
We can create functions using def statements. Their input is given in a function
call, and their output is given by a return statement.

                5 -->   square  --> 25
'''

# Defining Functions .........................................................

'''                   Function signature indicates name and number of arguments
                                /
                               /
        def     <   name  >  ( < parameters > ) :
                return  < return expression >
                                |
                        Funtion body defines the computation performed when the
                        function is applied
'''

def square(x):
    return x*x

y = square(-2)
y

'''
>>> radius = 10
>>> vol = (4/3)*pi*(radius**3)
>>> vol
4188.790204786391
>>> radius = 20
>>> vol
4188.790204786391
>>> def volume(r):
...     return (4/3)*pi*(r**3)
...
>>> volume
<function volume at 0x108fa9d90>
>>> volume(10)
4188.790204786391
>>> volume(20)
33510.32163829113
>>> volume(radius)
33510.32163829113
>>> def vol_ratio(r1,r2):
...     return volume(r1)/volume(r2)
...
>>> vol_ratio(20,10)
8.0
>>> vol_ratio(43441,2106)
8776.560310769528
>>> f = vol_ratio
>>> f(20,10)
8.0
>>> f
<function vol_ratio at 0x108fa9f28>
>>> vol_ratio
<function vol_ratio at 0x108fa9f28>
>>> vol_ratio = 10
>>> vol_ratio
10
>>> f(20,10)
8.0
>>> def vol_ratio(r1,r2):
...     return (r1**3)/(r2**3)
...
>>> vol_ratio(20,10)
8.0
>>> f
<function vol_ratio at 0x108fa9f28>
>>> vol_ratio
<function vol_ratio at 0x108fc3048>
>>>

Execution rule for 'def statements'
    1) Create a function with signature < name > ( < paramaters >)
    2) Set the body of that function to be everything indented after the first
    line
    3) Bind < name > to that function in the current frame
'''

# Functions in Environment Diagrams ...........................................

                                #                       Built-in Function
from operator import mul        # Global Frame                 /
def square(x):                  #        mul     ---->  func mul()
    return mul(x,x)             #       square   ---->  func square()
y = square(-2)                  #                               \
y                               #                       User defined function

'''
def statements are a type of a assignment that bind names to 'function values'
'''

# Calling User Defined Functions ..............................................

'''
Procedure for calling/applying user-defined functions (for now)
    1) Create a new 'Environment Frame'
    2) Bind the function's parameters to its arguments in that frame
    3) Execute the body of thw function in the environment
'''

''' Try this in Python Tutor
def square(x):
    return x*x
square(-2)
'''

# Putting it all together ....................................................

'''
1) Evaluate
    a. Evaluate the operator subexpression
    b. Evalueate each operand subexpression

2) Apply
    a. Apply the value of the operator subexpression to the values of the
    operand subexpression
'''

# Names & Environment ........................................................

'''
. Every expression is evaluated in the context of an environment
. An 'environment' is a 'sequence' of frames
. So far, there have been two possible environments:
    . The global frame
    . A function's local frame, then the global frame

Rules for looking up names in user-defined functions (version1)
    1) Look it up in the local frame
    2) If name isn't in local frame, look it up in the global frame.

'''

# Summary ....................................................................

'''
. Program consist of 'statements',or instructions for the computer, containing
'expressions', which describe computation and evaluate to 'values'.
. Values can be assigned to 'names' to avoid repeating computations.
. An 'assignment statement' assigns the value of an expression to a name in the
current 'environment'
. 'Functions' encapsulate a series of statements that maps 'arguments' to a
'return value'
. A 'def statement' creates a function object with certain 'parameters' and a 'body'
and binds it to a name in the current environment
. A 'call expression' applies the value of its 'operator', a function, to the
value(s) or its 'operand'(s), some arguments.
'''
