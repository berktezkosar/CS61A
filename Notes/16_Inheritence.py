#######################################
##            INHERITENCE            ##
#######################################
#        by  Alex Stennet


# Review ......................................................................

class A:
    x = 10
    def __init__(self, y):
        self.y = y
'''
>>> a = A(4)
>>> b = A(6)
>>> a.x = 5
>>>A.x
10
>>> b.x
10
>>> A.x = 15
>>> a.x
5
>>> b.x
15
'''

# Re-Implement Rationals .....................................................
'''
Rational class
    . Attributes
        . Numerator
        . Denominator
    . Methods:
        . print() - should print 'numerator / denominator'
        . add(other) - should return a new rational with addition of current and other
        . mul(other) - should return a new rational with multiplication of current
        and other
'''

from math import gcd

class Rational:
    def __init__(self, numerator, denominator):
        n = gcd(numerator, denominator)
        self.numerator = numerator // n
        self.denominator = denominator // n

    def print(self):
        if self.denominator == 1:
            print(self.numerator)
        else:
            print(self.numerator, '/', self.denominator)

# INHERITENCE  .................................................................
# An Energizing Example

'''
class Pokemon:
    """ A Pokemon."""
'''

'''
All Pokemon have:
    . a name                        -|
    . a trainer                      |
    . a level                        |  ATTRIBUTES
    . an amount of HP (life)         |
    . an attack: tackle             -|

Pokemon can:
    . say their name                 -|
    . attack other Pokemon            |  METHODS
    . recieve damage                 -|

'''

'''
class ElectricType:
    """An electric Pokemon."""
'''

'''
Electric-type Pokemon have:
    . a name                                             -|
    . a trainer                                           |
    . a level                                             | ATTRIBUTES
    . an amount of HP (life)                              |
    . an attack: thunder shock                           -|

Electric-type Pokemon can:
    . say their name                                     -|
    . attack 'and sometimes paralize' other Pokemon       | METHODS
    . recieve damage                                     -|
'''

class Pokemon:
    basic_attack = 'tackle'
    damage = 40

    def __init__(self,name,trainer):
        self.name,self.trainer = name, trainer
        self.level, self.hp = 1,50
        self.paralyzed = False

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        self.speak()
        print(self.name, 'used', self.basic_attack, '!')
        other.recieve_damage(self.damage)

    def recieve_damage(self,damage):
        self.hp = max(0,self.hp - damage)
        if self.hp == 0:
            print(self.name, 'fainted!')

class ElectricType:
    basic_attack = 'thunder shock'
    damage = 40
    prob = 0.1

    def __init__(self,name,trainer):
        self.name,self.trainer = name, trainer
        self.level, self.hp = 1,50
        self.paralyzed = False

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        self.speak()
        print(self.name, 'used', self.basic_attack, '!')
        other.recieve_damage(self.damage)
        if random() < self.prob and type(other) != ElectricType:
            other.paralyzed = True
            print(other.name, 'is paralyzed!')

    def recieve_damage(self,damage):
        self.hp = max(0,self.hp - damage)
        if self.hp == 0:
            print(self.name, 'fainted!')


'''there is whole bunch of repeated code now.
        Damage is same
        Both methods are same (__init__, recieve_damage)
    Only thing that is different between electric type and the normal type is
    attack and those variables on top.


What inheritance is going to let us do is remove code that is repeated by
leveraging other classes.
'''

# Class Relationships .........................................................

'''
Electric-type Pokemon are simply specialized versions of regular Pokemon!

basic_attack     |  /  basic_attack
damage           | /   swim
__init__         |                  basic_attack
speak            | =============>   prob
attack           | \                attack
recieve_damage   |  \
                    fly
'''

# Using Inheritance ...........................................................

'''
We can implement specialized classes using 'inheritance'!
The class definition allows us to specify that a new class inherits from a super
class:

                class < Class Name > (< Superclass Name >) :
                    < suite >

We call the more specialized class a 'subclass' of the general class and the
general class a 'Superclass' of the specialized class.

The subclass inherits all class attributes of the superclass.
'''

'''
>>> class A:
...     def __init__(self,x):
...             self.x = x
...     def double(self):
...             return self.x * 2
...
>>> class B(A):
...     def __init__(self):
...             self.x = 6
...
>>> a = A(2)
>>> a.double()
4
>>> b = B()
>>> b.x
6
>>> b.double()
12
'''

# New Dot Expression Rules ....................................................

'''
                    < expression > . < name >

How to evaluate:
    1) Evalueate < expression >, which yields an object.
    2) < name > is matched against the instance attributes of that object; if an
    attribute with that name exists, its value is returned.
    3) If not, the name is looked up in the class, which yields a class attribute
    value. 'If it is not found in the class, look in any superclasses.'
    4) That value is returned unless it is a function, in which case a bound method
    is returned instead.

>>> luxio = ElectricType('Luxio', 'Alex')
>>> luxio.hp            # Found in instance
50
>>> luxio.damage        # Found in Pokemon class
>>> luxio.basic_attack  # Found in ElectricType class
'thunder shock'
'''

'''


class Pokemon:
    basic_attack = 'tackle'
    damage = 40

    def __init__(self,name,trainer):
        self.name,self.trainer = name, trainer
        self.level, self.hp = 1,50
        self.paralyzed = False

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        self.speak()
        print(self.name, 'used', self.basic_attack, '!')
        other.recieve_damage(self.damage)

    def recieve_damage(self,damage):
        self.hp = max(0,self.hp - damage)
        if self.hp == 0:
            print(self.name, 'fainted!')


class ElectricType:
    basic_attack = 'thunder shock'
    damage = 40
    prob = 0.1

    def __init__(self,name,trainer):
        self.hp = 60

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        self.speak()
        print(self.name, 'used', self.basic_attack, '!')
        other.recieve_damage(self.damage)
        if random() < self.prob and type(other) != ElectricType:
            other.paralyzed = True
            print(other.name, 'is paralyzed!')

    def recieve_damage(self,damage):
        self.hp = max(0,self.hp - damage)
        if self.hp == 0:
            print(self.name, 'fainted!')
'''

'''
>>> a = ElectricType('a', 'b')
>>> a.hp
60
>>> a.name
File "<stdin>", line 1, in <module>
AttributeError: 'ElectricType', object has no attribute 'name'
'''

'''
class Pokemon:
    basic_attack = 'tackle'
    damage = 40

    def __init__(self,name,trainer):
        self.name,self.trainer = name, trainer
        self.level, self.hp = 1,50
        self.paralyzed = False

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        self.speak()
        print(self.name, 'used', self.basic_attack, '!')
        other.recieve_damage(self.damage)

    def recieve_damage(self,damage):
        self.hp = max(0,self.hp - damage)
        if self.hp == 0:
            print(self.name, 'fainted!')


class ElectricType(Pokemon):
    basic_attack = 'thunder shock'
    damage = 40
    prob = 0.1

    def __init__(self,name,trainer):
        #Pokemon.__init__(self,name,trainer)
        super().__init__(name,trainer)                         # Watch here!
        self.hp = 60

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        self.speak()
        print(self.name, 'used', self.basic_attack, '!')
        other.recieve_damage(self.damage)
        if random() < self.prob and type(other) != ElectricType:
            other.paralyzed = True
            print(other.name, 'is paralyzed!')

    def recieve_damage(self,damage):
        self.hp = max(0,self.hp - damage)
        if self.hp == 0:
            print(self.name, 'fainted!')
'''

'''
>>> a = ElectricType('b','c')
>>> a.name
'''

'''
>>> class A:
...     x = 6
...
>>> class B(A):
...     pass
...
>>> class C(B):
...     pass
...
>>> c = C()
>>> c.x
6
'''

# Designing for Inheritance .....................................................

'''
Don't repeat yourself; use existing Implementations
Attributes that have been overriden are still accesible via class objects
Look up attributes on instances when possible to allow for more specialization
'''

'''
def attack(self, other):
    Pokemon.attack(self,other)      # Reuse the general attack instead of rewriting
    if random() < self.prob and type(other) != ElectricType:
        other.paralyzed = True
        print(other.name, 'is paralyzed!')

Use self.prob over ElectricType.prob
'''

'''
class A:
    s = 'hello'
    def f(self):
        print(self.s)

class B(A):
    s = 'goodbye'

b = B()
b.f()
'''

# In Practice ..................................................................
##Tree ADT

def tree(label, branches = []):
    for b in branches:
            assert is_tree(b), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1 :
            return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent = 0):
    """ Prints levels of tree 't' indented by a space.
    >>> print_tree(tree(1))
    1
    >>> t = tree(3, [tree(1),
    ...              tree(2, [tree(1),
    ...                       tree(1)])])
    >>> print_tree(t)
    3
     1
     2
      1
      1
    """

    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def get_name(cls):
    return cls.__name__

def get_subclasses(cls):
    return cls.__subclasses__()

def subclass_tree(cls):
    branches = []

    for s_cls in get_subclasses(cls):
        try:
            branches.append(subclass_tree(s_cls))
        except TypeError:
                pass
    return tree(get_name(cls), branches)



'''
Errors built in Python;

>>> print_tree(subclass_tree(Exception))
Exception
 TypeError
 StopAsyncIteration
 StopIteration
 ImportError
  ModuleNotFoundError
  ZipImportError
 OSError
  ConnectionError
   BrokenPipeError
   ConnectionAbortedError
   ConnectionRefusedError
   ConnectionResetError
  BlockingIOError
  ChildProcessError
  FileExistsError
  FileNotFoundError
  IsADirectoryError
  NotADirectoryError
  InterruptedError
  PermissionError
  ProcessLookupError
  TimeoutError
  UnsupportedOperation
  ItimerError
 EOFError
 RuntimeError
  RecursionError
  NotImplementedError
  _DeadlockError
 NameError
  UnboundLocalError
 AttributeError
 SyntaxError
  IndentationError
   TabError
 LookupError
  IndexError
  KeyError
  CodecRegistryError
 ValueError
  UnicodeError
   UnicodeEncodeError
   UnicodeDecodeError
   UnicodeTranslateError
  UnsupportedOperation
 AssertionError
 ArithmeticError
  FloatingPointError
  OverflowError
  ZeroDivisionError
 SystemError
  CodecRegistryError
 ReferenceError
 BufferError
 MemoryError
 Warning
  UserWarning
  DeprecationWarning
  PendingDeprecationWarning
  SyntaxWarning
  RuntimeWarning
  FutureWarning
  ImportWarning
  UnicodeWarning
  BytesWarning
  ResourceWarning
 error
 Verbose
 Error
 _OptionError
>>>

Idea of defining a general class as a way to describe a very high level the
functionality to things that are very similar to it and then defining these
subclasses which are special versions of it.

It allows you generalize your code without reoeating it.
'''

# Practice ....................................................................

'''
Specification:
    . Dog Class
        - 4 legs
        - A name and owner's name
        - When calling .speak() should say 'woof!'
        - When calling .fetch() should say 'I fetched' + str(item)

    . Chicken Class
        - 2 legs
        - When calling .speak() should say 'cluck!'
        - A name and owner's name

    . GoldenRetriever Class
        - 4 legs
        - A name and owner's name
        - A breed equal to 'Golden Retriever'
        - When calling .speak() should say 'woof!'
        - When calling .fetch() should say 'I fetched' + str(item)
'''
class Animal:   # Superclass
    talk = 'I am an animal'

    def __init__(self, name, owner, legs):
        self.name = name
        self.owner = owner
        self.legs = legs

    def speak(self):
        print(self.talk)

class Dog(Animal):
    talk = 'woof!'
    breed = 'default'

    def __init__(self,name,owner):
        Animal.__init__(self, name,owner,4)

    def fetch(self, item):
        print('I fetched' + str(item))

class Chicken(Animal):
    legs = 2
    talk = 'cluck!'

class GoldenRetriever(Dog):
    breed = 'Golden Retriever'
