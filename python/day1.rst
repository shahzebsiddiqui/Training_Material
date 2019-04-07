=========
Day 1
=========

**Objective**: In this exercise, we will cover the basic on numbers, strings, list, conditional and looping, dictionary, sets, tuples, and string formatting

Setup
-------

- You need Python 3 for this exercise, you can check the version of python by running ``python -V``

Numbers
--------
Start a python interactive shell by running ``python`` and do the following

1. 1+1
2. 1+1.0
3. 10/3
4. 10//3
5. 20-5*4
6. (20-5)*4

Strings
---------

Create a file ``string.py`` and follow the exercise below

1. Define a string ``x`` and set it to some text 
2. Define a multiline string ``y`` and set a multi line string 
3. Retrieve length of string ``x``. See https://www.tutorialspoint.com/python3/string_len.htm for help 
4. Add two strings ``hello`` and ``world``
5. Retrieve first and last letter from string ``x`` defined in task 1
6. Declare a string with value ``abcdef`` and retrieve first and second letter, and 4th to end of string
7. Try adding "a" + 1. If you get error try to fix so output is ``a1``

List
-----

Create a file ``list.py`` and follow the exercise below

1. declare a list named ``alpha`` and assign ``a`` ``b`` ``c`` ``d``
2. declare two list ``x`` and ``y`` with 2, 4 and  8, 10 and do ``z=x+y``
3. Add +2 to each element of z
4. Multiply entire list by 2 try ``z*2``
5. Try the following ``a=[x*2 for x in z]``  and print value of ``a``
6. declare list ``a=[1,4,9,16]`` and clear list a. ``hint: empty list is []``
7. get length of a
8. declare list ``a=[1,4,9,16]`` and append "a",1.3,"hey"
9. declare ``a = [x for x in range(10)]`` and access every even value. ``hint: a[start_index:end_index:step]``

See https://docs.python.org/3/tutorial/datastructures.html#more-on-lists for more details on list operations

Conditional & Looping
-----------------------

Create file ``conditional.py`` and follow the exercise below

1. Declare variable ``x=2`` and print ``True`` if x is 2 otherwise print ``False``
2. Set variable a,b,c to True ``a=b=c=True`` and print ``True`` if all variable are ``True`` a
3. Set ``b=False`` and print ``True`` if a or b is ``True``
4. Set a string ``x="abcdef"`` and print ``short`` if length is less than 4 otherwise print ``long``
5. Repeat task 4 with a second condition if length is 6, print ``match``
6. Declare list ``x=["hi","how","is","your","day?"]`` and loop over list and print each item and length of string
7. Declare list ``a = [x for x in range(10)]`` and print each item until you reach ``7`` and break out of loop
8. Loop over same list and print value followed by ``odd`` or ``even`` depending on the number
9. Try the following ``print(list(range(5, 10)))``, ``print(list(range(20, 40,2)))``, ``print(list(range(-20, -60,-10)))``

Dictionary
------------

Reference: https://docs.python.org/3/tutorial/datastructures.html#dictionaries 

Create file ``dict_set_tuple.py``

1. Create a dictionary ``country`` with 2 keys ``USA`` and ``Canada`` with values ``New York`` and ``Toronto`` 
2. Access key ``USA`` from dictionary and print its value
3. Update key ``USA`` with value ``Boston``
4. Create a dictionary as follows ``dict={x: x**2 for x in (2, 4, 6)}`` and loop over dict and print key and value. See https://docs.python.org/3/tutorial/datastructures.html#looping-techniques for more details
5. Declare the for loop ``for i, v in enumerate(['tic', 'tac', 'toe']):`` and print the value of ``i`` and ``v``. For more details on **enumerate** see https://docs.python.org/3/library/functions.html#enumerate 

Tuple
------

Reference: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences 

1. Declare a tuple coord as follows  ``coord = (4,5,6,7,8)`` and access the first element
2. Declare a tuple ``empty=()`` and get its length
3. Declare ``vector = ((0,1),(2,3))`` and access first element
4. Loop over ``vector`` defined in task 7 and add +1 to X-coord and +2 to Y-coord

Sets
-----

Reference: 

- https://docs.python.org/3/tutorial/datastructures.html#sets 
- https://docs.python.org/3/library/stdtypes.html#set

1. Declare set ``state = {"CT","MA","CT"}`` and print the set 
2. Add ``NY`` ``PA``  ``NJ`` to set ``state`` 
3. Declare two sets ``europe`` and ``asia`` as follows and find union of set.

::

  europe = {"England", "France"}
  asia = {"India", "China"}

4. Let's get the intersection of two sets. Run the following ``print(set("abcd").intersection("ab"))``

String Formatting
------------------

Reference:

- https://pyformat.info/
- https://realpython.com/python-f-strings/

See ``string_format.py`` for examples on string formatting





      

