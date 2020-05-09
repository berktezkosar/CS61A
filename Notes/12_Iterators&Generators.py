#######################################
##      ITERATORS & GENERATORS       ##
#######################################

###########################
##      ITERATORS        ##
###########################

# Iterators ..................................................................
'''
Definitions
    Lazy Evaluations: Delays evaluation of an expression until its value is needed.
    Iterable: An object capable of returning its members one at a time. Examples
    include all sequences (lists, strings tuples) and some non-sequece types (dictionaries)
    Iterator: An object that provides sequencial access to values, one by one
        . All iterators are iterables. Not all iterables are iterators
    Metaphor: Iterables are book & iterators are bookmarks
'''
'''
>>> d = {1: "one", 2: "two", 3: "three"}
>>> for i in d:
...     print(i)
...
1
2
3
>>> d.keys()
dict_keys([1, 2, 3])
>>> for i in d:
...     print(d[i])
...
one
two
three
>>>
'''

'''
How do we create iterators?

iter(iterable): Return an iterator over the elements of an iterable value
    .This method creates a bookmark froom a book starting at the front.

next(iterable): Return the next element in an iterator.
    . Returns the current page and moves the bookmark to the next page
    . The iterator remembers where you left off. If the current page is the end
    of the book, error.

'''
'''
>>> bookmark = iter([1,2,3])
>>> next(bookmark)
1
>>> print("hello")
hello
>>> y = 5
>>> next(bookmark)
2
>>>
>>> next(bookmark)
3
>>> next(bookmark)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''
'''
>>> s = [1,2,3]
>>> one, two = iter(s), iter(s)
>>> next(one) # move bookmark 1
1
>>> next(two) # move bookmark 2
1
>>> next(one) # move bookmark 1
2
>>> next(two) # move bookmark 2
2
>>> three = iter(two)
>>> next(three) # move bookmark 2 & 3
3
>>> next(two) # run out of pages stop iteration
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
'''

# Check Your understanding: Fibonacci  ........................................

'''
Define a function that returns a n iterator that outputs up to the nth value in
the Fibonacci sequence. You can assume n will always be 2 or greater.
    .Remember, iter(iterable) creates an iterator. Lists are iterables.
'''

def fib_iter(n):
    '''
    >>> x = fib_iter(4)
    >>> next(x)
    0
    >>> next(x)
    1
    >>> next(x)
    1
    >>> next(x)
    2
    '''
    prev, curr = 0,1
    list = [prev, curr]
    index = 2
    while index < n:
        print(prev,curr)
        prev, curr = curr, prev + curr
        list += [curr]
        index += 1
    print(list)
    return iter(list)

'''
>>> x = fib_iter(5)
0 1
1 1
1 2
[0, 1, 1, 2, 3]
>>> next(x)
0
>>>
>>> next(x)
1
>>> next(x)
1
>>> next(x)
2
>>> next(x)
3
>>> next(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''

'''
>>> lst = [1,2,3,4]
>>> x = iter(lst)
>>> lst[0] = 0
>>> next(x)
0
>>> next(x)
2
>>>
'''

# Exceptions / Errors .........................................................
'''
Sometimes, computer programs behave in non-standard ways.
    . A function receives an argument value of an improper type
    . Some resources (such as a file) is not available
    . A network connection is lost in the middle of data transmission
'''

# Raise Exceptions ............................................................
'''
Exceptions are raised with a raise statement

            raise <expression>

<expression> must be an Exception, which is created like so:

E.g., TypeError('Error message')

TypeError - A function was passed the wrong number/type of argument
NameError - A name wasn't found
KeyError - A key wasn't found in a dictionary
RuntimeError - Catch all for troubles during interpretation
'''

def slices_per_friend(cake_slice_count, friend_count):
    try:
        result = cake_slice_count / friend_count
        return result
    except ZeroDivisionError as e:
        print(e)
        print("Please make a friend")
        return 0

# Back to Iterators - The For Statement  .....................................
'''
for <name> in <expression>:
    <suite>

1. Evaluate the header <expression>, which must evaluate to an iterable object.
2. For each element in that sequence, in order:
    a. Bind <name> to that element in the first frame of the current environment
    b. Execute the <suite>

When executing a for statement, iter returns an iterator and next provides each item:

>>> counts = [1, 2, 3]                  #     -|
>>> for item in counts:                 #      |
...     print(item)                     #      |
...                                     #      |==============|
1                                       #      |              |
2                                       #      |              |
3                                       #     -|              |
>>>                                                           | These are
>>>                                                           | equivalent!
>>> counts = [1,2,3]                    #     -|              |
>>> items = iter(counts)                #      |              |
>>> try:                                #      |              |
...     while True:                     #      |              |
...             item = next(items)      #      |              |
...             print(item)             #      |              |
... except StopIteration:               #      |============= |
...     pass                            #      |
...                                     #      |
1                                       #      |
2                                       #      |
3                                       #     -|
'''

###########################
##      GENERATORS       ##
###########################

# Definition and Rules ........................................................

'''
Some definitions:
    .Generator: An iterator created automatically by calling a generator function
    .Generator function: A function that contains keyword yield anywhere in the body

Ehen a generator funciton is called, it returns a generator instead of going into
the body of the function. The only way to go into the body of a generator function
is calling next on the returned generator.

Yielding values are the same as returning vales except yield remembers where it
left off.
'''

# Generators and Generator Functions ..........................................

'''
We are allowed to call next on generators because generators a type of iterator.
Calling next on a generator goes into the function and evalueates to the first
yield statement. The next time we call next on that generator, it resumes where
it left off (just like calling next on any iterator!)
Ince the generator hits a return statement, it raises a StopIteration

>>> def plusminus(x):
...     yield x
...     yield -x
...
>>> gen = plusminus(10)
>>> gen
<generator object plusminus at 0x102126ba0>
>>> next(gen)
10
>>> next(gen)
-10
>>> next(gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

>>> def plusminusfun(x):
...     x = x*x
...     yield x
...     x = x**6
...     yield x
...
>>> gen = plusminusfun(10)
>>> gen
<generator object plusminusfun at 0x102126b48>
>>> next(gen)
100
>>> next(gen)
1000000000000
>>> next(gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
>>> def gen_list(x):
...     yield x
...
>>> y = gen_list([1, 2, 3])
>>>
>>> next(y)
[1, 2, 3]
>>>

'''

# Generators to Represent Infinite Sequences ..................................

'''
Iterators are used to represent infinite sequences. In this course, when we ask
you to write an iterator, we want you to write a generator.

>>> def naturals():
...     x = 0
...     while True:
...             yield x
...             x += 1
...
>>> nats = naturals()
>>> next(nats)
0
>>>
>>> next(nats)
1
>>> next(nats)
2
>>> next(nats)
3
>>> next(nats)
4
>>> next(nats)
5
>>> nats1, nats2 = naturals(), naturals()
>>> [next(nats1) * next(nats2) for _ in range(5)]
[0, 1, 4, 9, 16] # Squares the first 5 natural numbers
>>>
'''

# Check Your understanding : Generators .......................................
'''
Givent the following generator function, what will the call to gen() return?

>>> def gen():
...     start = 0
...     while start != 10:
...         yield start
...         start += 1

>>> gen()
>>> x = gen()
>>> next(x)
'''

# Generators Can Yield From Iterators .........................................
'''
A yield from statement yields all values from an iterable

def a_then_b (a,b):                #                    |
    for x in a:                    #                    |
        yield x                    #                    |============|
    for x in b:                    #                    |            |
        yield x                    #                    |            |
                                                                     |
>>> x = a_then_b([1,2,3],["one","two","three"])                      |
>>> next(x)                                                          |
1                                                                    |
>>> next(x)                                                          |
2                                                                    |
>>> next(x)                                                          |
3                                                                    |
>>> next(x)                                                          |
'one'                                                                |
>>> next(x)                                                          |
'two'                                                                |
>>> next(x)                                                          |
'three'                                                              |
>>> next(x)                                                          |
Traceback (most recent call last):                                   |
  File "<stdin>", line 1, in <module>                                |
StopIteration                                                        |
>>> next(x)                                                          |
Traceback (most recent call last):                                   |
  File "<stdin>", line 1, in <module>                                |
StopIteration                                                        |
                                                                     |
                                                                     |
def a_then_b(a,b):                #                     |            |
    yield from a                  #                     | =========  |
    yield from b                  #                     | More convenient

>>> x = a_then_b([1,2,3],["one","two","three"])
>>> next(x)
1
>>> next(x)
2
>>> next(x)
3
>>> next(x)
'one'
>>> next(x)
'two'
>>> next(x)
'three'
>>>
'''

def countdown(k):
    if k ==0:
        yield 'Blast off'
    else:
        yield k
        yield from countdown (k-1)


# Summary .....................................................................

'''
We finally made it! What did we even talk about...
Iterators (bookmarks) are used to iterate over iterables (books).
    . We use iter method to turn iterables and we use the next method to get the
    next element.
Exceptions can be raised and handled.
Generators are jhow we implement iterators in this course and use yield statements
    We can use yield from the yield multiple values from an iterable.
'''
