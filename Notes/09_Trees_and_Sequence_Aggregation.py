######################################
##      SEQUENCE AGGREGATION        ##
######################################

# Iterable...............................................................
''' an object capable of returning its members one at time.
    Ex: all squences (lists,strings,tuples), some non-sequence types like
dictionaries

Several built-in functions take iterable arguments and aggregate them into a
value:
'''

    # sum(iterable[, start]) -> Value
'''
. Return the sum o f an iterable of numbers (NOT strings) plus the value of
parameter 'start' (which defaults to 0). When the iterable is empty, return
start.
. Note: cannot be called on strings instead must use built in string
method .join
'''

    # max(iterable[, key = func]) -> value OR max(a,b,c, ...[, key=func]) -> Value
'''
. With a single iterable argument, return its largest item
. With two or more arguments, return the largest argument

EXAMPLE ...............
>>>min([-4, -3, -2, -1, 0, 1, 2, 3, 4], key=lambda x:abs(x))
0
>>> f = lambda x: abs(x)
>>> f(-2)
2
>>> f(-1)
1
>>> min([-4, -3, -2, -1, 0, 1, 2, 3, 4], key=abs)
0
>>> min([(-2, 1), (-1, 2), (0, 3)], key=lambda x: x[1])
(-2,1)
'''

# More Sequence Aggregation.....................................................

    # bool (any_value) -> bool
'''
. Takes in any value (not only iterables) and returns True if the value os a True
value and False if it is a False value

EXAMPLE..................
>>> bool([])
False
>>> bool([1])
True
>>> bool([''])
True
'''

    # all(iterable) -> bool
'''
. Returns True if bool(x) is True for all vlues x in the iterable. If the
iterable is empty return True. In other words, checks if all values in the
iterable are true values.

EXAMPLE.......................
>>> all[1, 2, 3, 4, 5]
True
>>> [True, True, True, True, True, True, True]
True
>>> all([1, 2, 3, 0, 4, 5])
False
>>> any([1, 2, 3, 0, 4, 5])
True
>>> any([0, False, ''])
False
>>> any([0, False, '',1])
True
'''

    # any(iterable) -> bool
'''
. Returns True if bool(x) is True for at least one value x in the iterable.
If the iterable is empty, return False. In other words, checks if all values
in the iterable are true values.
'''

######################################
##             TREES                ##
######################################

# Tree Abstraction.............................................................

    # Recursive Description (Wooden Trees)
'''
A tree has a root and a list of branches
Each branch is a Tree
A tree with zero branches is called a leaf
'''

    # Relative Description
'''
Each location in a tree is called a node
Each node has a label value
One node can be the parent/child of another
'''
# Tree Abstraction Implementation .............................................

#               3
#              / \
#             1   2
#                /\
#               1  1

'''
>>> tree(3, [tree(1),
...          tree(2, [tree(1),
...                  tree(1)])])
[3, [1], [2, [1], [1]]]
'''

# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

######################################
##         TREE PROCESSING          ##
######################################

# Tree Processing Uses Recursion.............................................

'''
Just like checking for weather the branches were trees, we also use recursion
in tree processing functions.

1. The base case is the smallest version of the problem, many times if its a
leaf (though not always).
2. The recursive call happens on smaller subproblems, which tend to be branches
(though not always)
3. We use the recursive calls with some type of aggregation afterwards to
get our final solution
'''

# Count Nodes in a Tree ......................................................
''' We want to count how many nodes there are in this tree. Let's try recursively
'''
#                        8
#                      /  \
#                    4     3
#                   / \    / \
#                 2   3   1   1
#                            / \
#                           1   1

'''
1 + 3 + 5 = 9 ; there are 9 nodes in the entire Tree!
'''

ex1 = tree(8, [tree(4,[tree(2),tree(3)]),tree(3,[tree(1),tree(1, [tree(1),tree(1)])])])
ex2 = tree('D', [tree('B', [tree('A'),tree('C')]), tree('F', [tree('E'), tree('H', [tree('G'), tree('I')])])])


def count_nodes(t):
    if is_leaf(t):
        return 1
    total = 0
    for b in branches(t):
        total += count_nodes(b)
    return total + 1

'''
EXAMPLE

>>> ex1
[8, [4, [2], [3]], [3, [1], [1, [1], [1]]]]
>>> count_nodes(ex1)
9
'''

# Collect the Leaves ..........................................................

#                        D
#                     /    \
#                   B       F
#                 /  \    /   \
#               A    C   E    H
#                           /  \
#                          G    I

'''
Let's gather all the leaf values from this tree.
Again we tackle this recursively.

We notice that aggregation this time only requires the recursive calls; it does
not involve the original root.
'''

def collect_leaves(t):
    '''
    >>> collect_leaves(ex2)
    ['A', 'C', 'E', 'G', 'I']
    '''
    if is_leaf(t):
        return [label(t)]

    lst = []
    for b in branches(t):
        lst += collect_leaves(b)
    return lst

# Print Tree ..................................................................

'''
So far, trees appear as nested lists (because that is what they are underneath
the abstraction barrier). Let's implemet a function that prints out the tree
more visuall!
'''

#                 3
#              /    \
#             1       2
#           /  \    /   \
#          0   1   1    1
#                      / \
#                     0  1

def print_tree(t, indent=0):
    '''
    >>> print_tree(fib_tree(4))
    3
     1
      0
      1
     2
      1
      1
       0
       1
    '''
    if is_leaf(t):
        print(' '*indent, label(t))
    else:
        print(' '*indent, label(t))
        for b in branches(t):
            print_tree(b, indent + 1)

def print_calls(name, f):
    def new_f(t):
        print('Name:', name)
        print('Imputted Tree:')
        print_tree(t)
        input()
        ret = f(t)
        print('Returned', ret)
        return ret
    return new_f

collect_leaves = print_calls('collect_leaves', collect_leaves)

######################################
##         CREATING TREES           ##
######################################

'''
A function that creates a tree from another tree is typically also recursive
Let's create a function that returns a new tree with every value squared.
'''
#               8                            64
#             /  \                          /  \
#           4     3         =====>        16     9
#          / \    / \                    / \    / \
#        2   3   9   6                 4   9   81  36
#
''' Common Approach: Let's get into a recursive mindset.
'''

# The Recursive Process

#               8
#             /   \
#           4      3
#          / \    / \
#        2   3   9   6
#
#          |        |
#          |        |
#          |        |
#          v        v             |--------------------------------------|
#              64        =======> |Join the 2 new subtrees with the root |
#           /      \              |values squared                        |
#          16       9             |--------------------------------------|
#         / \      / \
#       4   9    81   36
#
# | Recursively| | Recursively  |
# | create the | | create the   |
# | squared    | | next squared |
# | subtree    | | subtree      |
#


def square_tree(t):
    '''

    >>> square_tree(tree(2))
    tree(4)
    '''
    if is_leaf(t):
        return tree(label(t)**2)

    lst = []
    for b in branches(t):
        lst += [square_tree(b)]

    return tree(label(t)**2, lst)

# Fib Tree
'''
Let's define fib_tree(n) to have fib(n) as the label; and its subtrees are
fib_trees as well.

Reminder fib sequence: 0, 1, 1, 2, 3, ...

Ex: n=4
'''

#               3   --------------- Label is sum of labels of subtrees
#              / \
#             1   2
#           / |  / \
#          0  1 1  1
#                 / |
#            |    0  1
#            |
#            |      |
#   fib_tree(2)     |
#                   |
#                   |
#                fib_tree(3)

def fib_tree(n):
    if n <= 1:
        return tree(n)

    left = fib_tree(n-2)
    right = fib_tree(n-1)
    return tree(label(left) + label(right), [left, right])
