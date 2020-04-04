#######################################
##  OBJECT-ORIENTED PROGRAMMING - I  ##
#######################################

# Object Oriented Programming

'''
A method for organizing modular programs and represent the real world.
    . Data abstraction
    . Bundling together information and related behavior.

A metaphor for computation using distributed state
    . Each object has its own local state
    . Each object also knows how to manage its own local state
    . Method calls are messages passed between objects
    . Several object may all be instances of a common type
    . Different types may relate to each other

Specialized syntax & vocabulary to support this metaphor
'''

# Classes .....................................................................

'''
A class serves as a template or blueprint for its instances

    Idea: All blank accounts have a balance and an account holder; the Account
    class should add those attributes to each newly created instance.

    Idea: All bank accounts should have 'withdraw' and 'deposit' behaviors that
    all work in the same way.

    Better Idea: All bank accounts share a 'withdraw' and 'deposit' method.

    All accounts might also share other characteristics like maximum withdraw,
    or loan limit.
'''

'''
>>> a = Account('James')
>>> a.holder
'James'
>>> a.balance
0
'''

'''
>>> a.deposit(15)
15
>>> a.withdraw(10)
5
>>> a.balance
5
'''

# The Class Statement  ........................................................

'''
A class statement creates a new class and binds that class to the current
environment.

Assignment & def statements in the <suite> create class attributes
'''

'''
class <name>:
    <suite>
'''

#class Account:
#    max_withdrawal = 10
#    def deposit(...):
#        ...
#    def withdraw(...):
#
#
#

#   Global Frame |
#   -------------|
#
#        Account |_
#                   \
#                    \
#                     \
#                   Account class
#                  ====================
#                         max_withdrawal  | 10 |
#                                deposit  |    | =====> func deposit(...) [p=G]
#                               withdral  |    | =====> func withdraw(..) [p=G]



'''
Before we start implementing our methods, we need to talk about how to create
Accounts

Idea: All bank accounts have a balance and an account holder. There are not shared
across Accounts.

When a class is called:
    1. A new instance of that class is created
    2. The __init__ method of a class is called with the new object at its first
    argument (named self), along with arguments provided in the call expression.
'''

class Account:
    pass
    def __init__(self, account_holder):  # __init__ is called the constructor
        self.balance = 0
        self. balance = account_holder
    pass


class Account:
    max_withdrawal = 10

    def __init__ (self, account_holder):
        self.balance = 0
        self.balance = account_holder

    def deposit(self, amount):
        pass

    def withdraw(sel, amount):
        pass

a = Account('James')


'''
   Global Frame |
   -------------|
                                    ->   Account Instance
        Account |_                /     ==================
            a   |_ \    ----------      balance | 0
                    \                    holder | 'James'  #Instance Attributes  <=
                     \                                                             |
                      \                                                            |
                       \                                                           |
                   Account class                                                   |
                  ====================                                             |
                         max_withdrawal  | 10 |                                    |
                                __init__ |    | =====> func                        |
                                deposit  |    | =====> func deposit(...) [p=G]     |
                               withdral  |    | =====> func withdraw(..) [p=G]     |
                                                                                   |
                  f1: __init__ [p=G]                                               |
                  =====================                                            |
                            self|_                                                 |
                  account_holder|_ 'James'                                         |
                    Return Value|_ None     ========================================
'''

# Object Identity .............................................................

'''
Every object tht is an instance of a user-defined class has a unique identity:

    >>> a = Account('James')
    >>> b = Account('John')
    >>> c = Account('James')

Identity operators 'is' and 'is not' test if two expressions evaluate to the same
object (the arrows point to the same place)

    >>> a is a
    True
    >>> a is not b
    True
    >>> c is a
    False
    >>>

Binding an object to a new name using assignment does not create a new object.

    >>> d = a
    >>> d is a
    True
'''

# Dot Expressions .............................................................

'''
You can access class or instance attributes with dot notation.

            <exoression> . <name>

The <expression> can be any valid Python expression that evaluates to a class or
instance. The <name> must be a simple name.

To Evalueate a dot expression:
    1. Evaluate the to the left of dot, which yields the object of the dot
    expression
    2. <name> is matched against the instance attributes of that object, if an
    attribute with that name exists, value is returned.
    3. If not, <name> is looked up in the class, which yields a class attribute
    value
    4. That value is returned unless it is a function, in which case a bound
    method is returned instead.
'''

class Account:
    max_withdrawal = 10

    def __init__ (self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        pass

    def withdraw(sel, amount):
        pass

a = Account('James')
print(a.balance)
print(a.holder)
print(a.max_withdrawal)
# print(Account.balance)
print(Account.__init__)
print(Account.deposit)
print(a.deposit)


# Methods and Functions ......................................................

'''
'Methods' are functions defined in the suite of a class statement.

However methods that are accessed through an instance will be bound methods.
'Bound methods' cou[le together a function and the object on which that method
will ve invoked. This means that when we invoke bound methods, the instance is
automatically passed in as the first argument.

    >>> a = Account('James')
    >>> Account.deposit
    <function>
    >>> a.deposit
    <method>
'''

# Invoking Methods ............................................................

'''
We can call class methods in two ways: as a bound method and as a function.

Invoking class methods as a bound method:
    - Bound metgods are accessed through the instance and implicity pass the
    instance object in as the first argument of the method.
    - <instance> . <method_name> (<arguments>)
    - Ex. a.deposit(5) => a gets passed in to the deposit function as the first argument

Invoking class methods as functions:
    - We can use the class name to directly call a method. These follow our
    typical function call rules and nothing is implicity passed in.
    - <class_name> . <method_name>(<instance>,<arguments>)
    - Ex. Account.deposit(a,5)
'''

# Implementing the Account Class ..............................................

class Account:
    max_withdrawal = 10
    def __init__(self,account_holder):
        '''Creates an instance of Account class'''
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        '''Deposits amount to the account'''
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        '''Subtracts amount from the account'''
        if amount > self.max_withdrawal or amount > self.balance:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance

# Accessing Attributes ........................................................

'''
There are built-in functions that can help us access attributes.
Using getattr, we can look up an attribute using a string instead.
    - getattr(<expression> . <attribute_name(string)>)
    - getattr(a,'balance') is the same as a.balance
    - getattr(Account,'balance') is the same as Account.balance

Using hasattr, we can check if an attribute exists.
    -hasattr(<expression> . <attribute_name(string)>)
    -hasattr(a,'balance') return True
    -hasattr(Account,'balance') returns False

We saw this before, but let's formalize the rules for assigning/re-assigning
instance and class attributes.

<expression> . <name> = <value>

Change attributes for the 'object of that dot expression'

'If the expression evalueates to an instance': then assignment sets an instance
attribute, even if it exists in the class.

'If the expression evaluates to a class': then the assignment sets a class attribute
'''

# Summary ........................

'''
. Object-oriented programming is another way (paradigm) to organize and reason about
programs.
. The Python 'class' statement allows us to create user-defined data types that
can be used just like built-in data types
    . Class attributes are variables shared across instances
    . Instance attributes are unique to each instance
    . Two ways to invoke methods, implicity and explicitly.
    . Tomorrow, we'll discover how to define the relationships between Different
    classes

. In lab you'll use OOP to make a trading card game!
'''

#######################################
##  OBJECT-ORIENTED PROGRAMMING - II ##
#######################################

# Review: Object Oriented Programming .........................................

'''

Objects:
    We've already seen some examples of Python's built-in objects:

>>> lst = [1, 2, 3, 4] # Assigns a list object to a name
[1, 2, 3, 4]
>>> lst.pop(2)         # list method
3
>>> lambda x: x + 3    # Creates a function object
<function <lambda> ... >

Object oriented programming: a paradigm for programming based on objects with
attributes and methods

We can modularize our programs by writing our own 'classes' for objects!
'''

# User - Defined Objects ......................................................

'''
Example: We want to represent a bank account for a given user with a balance.
A user should be able to withdraw from and deposit to an account, which updates
the balance.
'''

'''
>>> a = Account('Tammy')
>>> a.holder
'Tammy'
>>> a.balance
0
>>> a.deposit(100)
100
>>> a.balance
100
>>> a.withdraw(10)
90
'''

# Check your understanding .....................................................

class Foo:
    a = 5

    def __init__(self,a):
        self.a = a
        self.b = 'hi'

    def g(self,x):
        self.a += x

    def h(self,y):
        return self.b[y]

'''Answer the following questions about the Foo class:
    1) What are the class attributes of Foo
    2) What are the instance attributes of a Foo instance
    3) Given an instance of Foo named f, what are two ways of calling the method
    g on f, passing in 3?
    4) What would Python display?
'''

''' Answers of the questions:
    1) a, __init__, g,h
    2) a,b
    3) f.g(3) Bound Method,
       Foo.g(f,3) Function
    4)
        >>> f = Foo(10)
        >>> f.a
        10
        >>> Foo.a
        5
        >>> f.h(1)
        'i'
'''

#######################################
##         MUTATING OBJECTS          ##
#######################################

# Objects State ...............................................................

'''
>>> a1 = Account('Tammy')
>>> a2 = Account('James')
>>> a1.balance
0
>>> a2.balance
0
>>> a1.deposit(100)
100
>>> a2.deposit(200)
200
>>> a1.withdraw(40)
60
>>> a2.withdraw(10)
190
'''

# Assigning Attributes ........................................................

'''
Recall that to 'mutate' an object is to change its state

We can change an object's state by assigning new attributes or reassigning
existing ones. (This is done in the methods of 'Account'!)

    < obj_expression> . < name > = < expression >

- If < obj_expression > evaluates to a class, then a class attribute is assigned.
- If < obj_expression > evaluates to an instance, then an instance attribute
is assigned.
'''

'''
    Account Class:                                      Account Instance:
    ===============                                     =================
    max_withdrawal: 50                                  holder: 'Tammy'
                ...                                    balance:  0


>>> a = Account('Tammy')
>>> Account.max_withdrawal = 40

    Account Class:                                      Account Instance:
    ===============                                     =================
    max_withdrawal: 50                                  holder: 'Tammy'
                ...  40                                balance:  0

>>> a.max_withdrawal = 20

    Account Class:                                      Account Instance:
    ===============                                     =================
    max_withdrawal: 50                                  holder: 'Tammy'
                ...  40                                balance:  0
                                                max_withdrawal:  20
'''
