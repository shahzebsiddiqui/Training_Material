modulefile exercise 1
=====================


Approx Time: 10mins

Please source the following file before proceeding

.. code::

   source setup.sh


In this exercise, check out each modulefiles as you proceed with the instructions to
see how ``module`` command interact with modulefiles


You can check the content of the module file using ``module show --raw modulefile`` or 
use any linux command like ``cat`` ``view`` ``vim``

Example: module help example

.. code::

        module help a
        ml a


Example: prereq example. module b depends on module a. Loading b without a will cause
 an error

.. code::

        ml purge
        ml a 
        ml b

        ml purge
        ml b

Example: conflict modules 

.. code::

        ml help c
        ml whatis c

        ml purge
        ml c

        ml purge
        ml a c
        ml c a

There is a conflict on module a when loading module c but not the otherway around 
so ``ml c a`` will work but ``ml a c`` will not work


Example: Loading dependent modules. Note how dependent modules behave upon load
and unload operation

.. code::

        module purge
        module load d
        module list
        module unload d
        module list

Example: Same example as before but with conditional prior to load

.. code::

        module purge
        module load e
        module list
        module unload e
        module list

Example: LmodMessage example 

.. code::

        ml purge
        ml f

Example: Declaring an alias inside modulefile 

.. code::

        ml purge
        ml g
        cpu
        ml -g
        cpu


Example: Introspection Function and executing Linux commands from modulefile

.. code::

        ml purge
        ml h
        module unload h



