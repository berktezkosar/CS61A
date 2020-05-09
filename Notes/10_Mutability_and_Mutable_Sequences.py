'''
# Where are we in CS61A

Building Blocks' of PRograms
Managing Complexity
Representıng Collectıons of Data

What are Containers Good for?
  . Allow us to store related valeus together
       .can process the values one-by-one or ın aggregate
       .Allows us to form compound values throufg data abstractıon
  . Give rise to a number of ways of storing values
       . Lists store values in order, associated with an index
       . Dictionaries have no order but associate values with any sort of key
       . Trees allow for a hierarchical representation of Data

The Many Uses of Trees
 Trees show up in:
  . Efficiency searching data (e.g. Autocomplete)
  . Artificial Intelligence (Game Trees / the minimax algorithm)
  . Machine Learning (Decision Trees)
  . Computational Biology (Suffix Trees, Phylogenetic Trees)
  . Programming Languages (Syntax and Expression Trees)
  . Operating Systems (File Structure)

'''
#            Desktop    ==> Each node contains a file or directory
#           /       \
#   tree.py        CS61A
#                 /     \
#               Labs    Projects
#               \
#              lab00.py    ====> Children of a node are files/directories
#                                contained in that directory
#
#             'h'    ==> Each node contains a string (possibly representing a word)
#          /       \
#     'home'       'ha'
#                /     \
#              'har'    'ham'
#              /    \
#         'harm'    'hard'    ====> Children of a node contain words/strings
#                                   starting with the same prefix
#
#
#

#######################################
##            MUTABILITY             ##
#######################################

# Using Compound Values ......................................................
'''
. Data abstraction allows us to think about compound values as units, or 'objects'.
. But compound values have 'state' that change over time; they are 'mutable'
. So far, we treated all our values are 'immutable'; we only created new objects,
never changing them.
'''
'''
EXAMPLE

>>> queue[1:]
['Daredevil', '']
>>> queue = ['Black Mirror', 'Daredevil','The Office']
>>> queue[1:]
['Daredevil', 'The Office']
>>> queue
['Black Mirror', 'Daredevil', 'The Office']
>>> new_queue = queue[1:]
>>> new_queue
['Daredevil', 'The Office']
>>> queue
['Black Mirror', 'Daredevil', 'The Office']
>>> newer_queue = new_queue + ['Stranger Things']
>>> newer_queue
['Daredevil', 'The Office', 'Stranger Things']
>>> new_queue
['Daredevil', 'The Office']
>>> queue2020 = newer_queue[:1] + newer_queue[2:]
>>> queue2020
['Daredevil', 'Stranger Things']
>>> newer_queue
['Daredevil', 'The Office', 'Stranger Things']
>>>
'''

# Making New Objects ..........................................................

to_five = [1, 2, 3, 4, 5]
to_four = to_five[:4]
to_six = to_five
to_six = to_six + [6]     # Only make new lists
to_neg_five = [-x for x in to_five]
same = to_five # New variable pointing to same list

#######################################
##        MUTATION OPERATIONS        ##
#######################################
'''
EXAMPLE
>>> lst = [6, 1, 'b']
>>> lst
[6, 1, 'b']
>>> lst[2] = 'a'
>>> lst
[6, 1, 'a']
>>> lst.append(2)
>>> lst
[6, 1, 'a', 2]
>>> lst.extend([0, 1, 9])
>>> lst
[6, 1, 'a', 2, 0, 1, 9]
>>> lst.insert(3, 'summer')
>>> lst
[6, 1, 'a', 'summer', 2, 0, 1, 9]
>>> a = lst.append(7)
>>> lst
[6, 1, 'a', 'summer', 2, 0, 1, 9, 7]
>>> print(a)
None
>>> new_list = [1]
>>> new_list.extend(range(10))
>>> new_list
[1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> new_lst = [1]
>>> new_lst.append([1, 2])
>>> new_lst
[1, [1, 2]]
>>> new_lst.insert(1, [3, 4])
>>> new_lst
[1, [3, 4], [1, 2]]
>>> new_lst
[1, [3, 4], [1, 2]]
>>>
>>> lst
[6, 1, 'a', 'summer', 2, 0, 1, 9]
>>> lst.append([7])
>>> lst
[6, 1, 'a', 'summer', 2, 0, 1, 9, [7]]
>>> lst = [6, 1, 'a', 'summer', 2, 0, 1, 9]
>>> lst.append(7)
>>> lst
[6, 1, 'a', 'summer', 2, 0, 1, 9, 7]
>>> lst.pop()
7
>>>
>>> lst
[6, 1, 'a', 'summer', 2, 0, 1, 9]
>>> b = lst.pop(3)
>>> lst
[6, 1, 'a', 2, 0, 1, 9]
>>> b
'summer'
>>> lst.remove(6)
>>> lst
[1, 'a', 2, 0, 1, 9]
>>> lst.remove(1)
['a', 2, 0, 1, 9]
>>> lst.remove(1)
>>> lst
['a', 2, 0, 9]
>>> c = lst.remove(0)
>>> c
>>> print(c)
None
>>> [1, 2, 3, 1, 4, 5, 1]
[1, 2, 3, 1, 4, 5, 1]
>>> [x for x in [1, 2, 3, 1, 4 ,5, 1] if x != 1]
[2, 3, 4, 5]
>>> lst = [1, 2, 1, 2, 3, 1]
>>> while 1 in lst:
...     lst.remove(1)
...
>>> lst
[2, 2, 3]
>>>
'''

# List Mutation ................................................................

    # append(el): adds el to the end of the list
    '''
    >>> lst = [1, 2, 3, 4, 5]
    >>> lst.append(6)
    >>> lst
    [1, 2, 3, 4, 5, 6]
    '''

    # insert(i, el): inserts el at index i
    '''
    >>> lst = [1, 2, 3, 4, 5]
    >>> lst.insert(2, 2.5)
    >>> lst
    [1, 2, 2.5, 3, 4, 5]
    '''

    # extend(seq): adds elements in seq one by one to the end of the list
    '''
    >>> lst = [1, 2, 3]
    >>> lst.extend([4, 5])
    >>> lst
    [1, 2, 3, 4, 5]
    '''

    # remove(el): removes the first occurance of el from the list
    '''
    >>> lst = [1, 2, 3, 2, 5]
    >>> lst.remove(2)
    >>> lst
    [1, 3, 2, 5]
    '''

    # pop(i): removes and returns the element at index i
    '''
    >>> lst = [1, 2, 3, 4, 5]
    >>> lst.pop(3)
    4
    >>> lst
    [1, 2, 3, 5]
    '''

'''
EXAMPLE
>>> d = {"M" : "Alex",
...     "W" : "Tiffany",
...     "Th" : "Chris"}
>>> d["M"]
'Alex'
>>> d["Th"]
'Chris'
>>> d["T"] = "Tiffany"
>>> d
{'M': 'Alex', 'W': 'Tiffany', 'Th': 'Chris', 'T': 'Tiffany'}
>>> d["W"] = "Alex"
>>> d
{'M': 'Alex', 'W': 'Alex', 'Th': 'Chris', 'T': 'Tiffany'}
>>> "F" in d
False
>>> "W" in d
True
>>> "Tiffany" in d
False
>>> d.items()
dict_items([('M', 'Alex'), ('W', 'Alex'), ('Th', 'Chris'), ('T', 'Tiffany')])
>>> d.values()
dict_values(['Alex', 'Alex', 'Chris', 'Tiffany'])
>>> "Tiffany" in d.values()
True
>>> d.keys()
dict_keys(['M', 'W', 'Th', 'T'])
>>> "a"
'a'
>>> 'a'
'a'
>>> d['W'] = [d['W']] +['Tiffany']
>>> d['W']
['Alex', 'Tiffany']
>>>
>>> lst = ['a', 'b', 'c', 'd']
>>> letters = {}
>>> for i in range(len(lst)):
...     letters[lst[i]] = i + 1
...
>>> lst
['a', 'b', 'c', 'd']
>>> letters
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> letters[['e', 'f']] = 5
Traceback (most recent call last):      ======> key of the dict is not mutable
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>>

'''

#######################################
##          IMMUTABLE VALUES         ##
#######################################

'''
>>> s = 'cs61b'
>>> s[4]
'b'
>>> s[4] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> s.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'pop'
>>> s.append()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'append'
>>> s.append('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'append'
>>> s = 'cs61a'
>>> s
'cs61a'
>>> s = 'cs61a' - 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> t = (1, 2, 3, 4)
>>> t
(1, 2, 3, 4)   ============> TUPLE
>>> t[2]
3
>>> t[:1]
(1,)
>>> t[1:]
(2, 3, 4)
>>> t[0]
1
>>> t[0] = 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t.append(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> t2 = 1, 2, 3, 4
>>> t2
(1, 2, 3, 4)
>>> def f():
...     return 1,2
...
>>> x,y = f()
>>> x
1
>>> y
2
>>> f()
(1, 2)
>>> x,y = (1,2)
>>> x
1
>>> y
2
>>> type((1,2))
<class 'tuple'>
>>>
'''

#######################################
##      MUTATING WITH FUNCTIONS      ##
#######################################

def mystery(lst): # mutative function
    lst.pop()
    lst.pop()

''' You can try this in Python Tutor
>>> four = [4, 4, 4, 4]
>>> mystery(four)
>>> four
[4, 4]
>>>
'''

def mystery2(x): # mutative function
    lst.append(x)
    lst.append(x)

'''
>>> lst = [4, 4]
>>> mystery2(5)
>>> lst
[4, 4, 5, 5]
>>>
'''

#######################################
##      IDENTITY VERSUS EQUALITY     ##
#######################################

# Identity ....................................................................
'''
<expr0> is <expr1>

evaluates to True if both <expr0> and <expr1> evaluate to the same object
'''

# Equality  ....................................................................
'''
<expr0> == <expr1>

evaluates to True if both <expr0> and <expr1> evaluate to equal values
'''


'''
EXAMPLE

>>> l1  = [1, 2, 3]
>>> l2  = [1, 2, 3]
>>> l1 is l2
False
>>> l3 = l1
>>> l3 is l1
True
>>> l1 == l2
True
>>> l3 == l1
True
>>> l3
[1, 2, 3]
>>> l1
[1, 2, 3]
>>> l1[0] = 0
>>> l1
[0, 2, 3]
>>> l3
[0, 2, 3]
>>> l3 is l1       ====> l3 still identical to l1
True                     identical variables will all be updated if you mutate
>>>                      any of them
>>> l2
[1, 2, 3]
>>> l1 == l2
False
>>> l1 = l2[:]  ======> Slicing always creates a new list
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1 is l2  =======> Therefore it is false
False
>>>
'''

# Identity vs. Equality in Environmental Diagrams
'''
Review: for assignment statements, evaluatethe right side, then assign to the left.
Copying: when creating a copy, copy exactly what's 'in the box'
'''

''' Copy this code to the Python Tutor and try yourself!
>>> lst1 = [0, 6, [-2, 4]]
>>> lst2 = lst1
>>> lst3 = lst1[1:]
'''

''' Copy this code to the Python Tutor and try yourself!
EXAMPLE
>>> lst1 = [0, 6, [-2, 4]]
>>> lst2 = lst1
>>> lst3 = lst1[1:]
>>> lst1 = [1, [2,3], 4]
>>> lst2 = lst1
>>> lst3 = lst1[:]      =======>  Same as lst1[0:len(lst1)]
>>> lst1[0] = 10
>>> lst3[2] = 40
>>> lst2[1][1] = 30
>>> lst2.pop(1)
>>> lst1.append(lst3)
>>> print(lst1)
>>> print(lst2)
>>> print(lst3)
'''
