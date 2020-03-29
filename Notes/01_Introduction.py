###########################
##      EXPRESSIONS      ##
###########################

# Types of Expressions .......................................................
'''
An exoression describes a computation and evaluate to a value.

 18 + 45                f(x)                2^100

        (2334683)^*(1/2)            |-1253|
'''

# Call Expressions in Python ..................................................

'''
All expressions can use function call.
'''

''' EXAMPLE
>>> 2019
2019
>>> 2000+19
2019
>>> 0+1//2+3+4*((5//6)+7*8*9)
2019
>>> max(2,4)
4
>>> min(-2, 5000)
-2
>>> from operator import add,mul
>>> add(2,3)
5
>>> mul(2,3)
6
>>> max(1,2,3,4,5)
5
>>> max(add(2,mul(4,56)),add(3,6))
226
>>>
'''

# Anatomy of a Cell Expressions ..............................................

'''
        add (   2   ,     3)
         |      |         |
    operator  Operand    Operand
'''

# Evaluation of a Call Expression ............................................

'''
1) Evaluate
    a) Evaluate the operator subexpressions
    b) Evaluate each operand subexpressions
2) Apply
    a) Appy the value of the operator subexpression to the values of the operand
    subexpression
'''

###  Nested Call Expressions .................................................

'''                     45
            add(add(6,mul(4, 6)), mul(3,5))
                    30                      15
            add ( 6, mul(4,6)          ,    mul(3,5))
                        24
            add   6   mul(4,6)               mul 3    5

                      4     6
'''
