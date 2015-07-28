# Types & Operations
Mutable types are those that have operations that mutate or update part of the value. Other types are immutable. Numbers, Booleans, strings, tuples, and functions are immutable, while all other types are mutable.

Null Object
-------
The single value None is known as the null object. Its type is the NoneType. It serves as a placeholder return value for functions that would otherwise return nothing. It is also used as an special argument value to some operations, such as filter() and a_str.split().

Integers & Floating-Point Numbers
-------
Integers have a limited number of digits, whereas long integers can have an arbitrary number of digits. Operations that normally produce an integer will instead produce a long integer, if more digits are needed. Operations on long integers are slower than on other numbers.

Floating-point numbers have a decimal point and a limited number of digits. Arithmetic operations on floating-point numbers can give somewhat inaccurate results because of the limited precision.

Booleans
-------
Booleans represent the logical truth values True and False. Expressions that evaluate to Boolean values are especially used as the tests in conditionals (if boolean_expr: …).

While not encouraged, Booleans can also be used anywhere that numbers can. True and False are then treated as 1 and 0, respectively.

Strings
-------
A string is an immutable sequence of characters. Many characters are familiar from what you can type on a keyboard — a letter, a number, a symbol, or a space. The string with zero characters is called the empty string.

Lists
-------
A list is a mutable sequence of values of any type. A list with zero elements is called an empty list. List elements are indexed by sequential integers, starting with zero.

Tuples
-------
A tuple is an immutable sequence of values of any type. Tuple elements are indexed by sequential integers, starting with zero.

Dictionaries
-------
A dictionary is a mutable mapping from keys to values. A dictionary with no keys is called an empty dictionary. Dictionaries are also known in some programming languages as associative memories, associative arrays, or hashmaps. Unlike sequences, which are indexed by a range of integers, dictionaries are indexed by keys, which can be of any immutable type. Thus, dictionaries are also unordered. When printed, iterated upon, or converted into a sequence, its elements will appear in an arbitrary, implementation-dependent order.

Sets
-------
A set is an unordered collection without duplicates. When printed, iterated upon, or converted into a sequence, its elements will appear in an arbitrary, implementation-dependent order.

Functions & Methods
-------
A function is a parameterized section of code. A method is simply a function which is an attribute of an object, i.e., defined as part of a class. Functions and methods are values themselves. (However, CodeSkulptor does not yet consider built-in functions to be values.)

Generators
-------
Generators are a kind of iterator that are defined like functions. A generator function looks just like a regular function, except that it uses yield instead of return.

File Objects
-------
This module contains functions for obtaining input data from the web. Currently, CodeSkulptor's implementation of this module supports input only, not output, and only from a a CodeSkulptor-affiliated data storage site. To use these operations, first import the module with import urllib2.

File objects represent open files. A file object keeps track of the current position in the file. Each read operation gets data starting at this position and advances the position to the end of the returned data. CodeSkulptor only supports obtaining an open file via urllib2.urlopen().

Enumerations
-------

Iterators
-------
Iterators are a kind of iterable, and thus support iteration or looping — e.g., for x in an_iter. Such a loop implicitly calls an_iter.next() repeatedly to get each element from the iterator, thus exhausting the elements in the iterator. Similarly, calling functions such as list() on an iterator will implicitly loop through and exhaust the iterator.

Sequences
-------
Sequences are ordered collections of data. Their elements can be indexed by integers indicating positions.

Iterables
-------
Iterables are collections of data that allow iteration or looping — e.g., for x in an_iter.

Objects
-------
