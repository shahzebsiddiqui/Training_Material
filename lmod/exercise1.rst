Exercise 1
==========

Approx Time: 10 mins

View all modules in system

.. code::

        module av

Search for a module gcc

.. code::

        module av gcc


Try loading a module

.. code::

        module purge
        module load intel
        module list

Try loading multiple modules

.. code::

        module purge
        module load Go
        module load Anaconda2
        module list

Try loading two modules in one command

.. code::

        module purge
        module load Go Anaconda2
        module list


Try swaping one module with another

.. code::

        module purge
        module load Go Anaconda2
        module list
        module swap Go Inspector
        module list


Swap with ``sw`` and ``switch``

.. code::

        module purge
        module load Go Anaconda2
        module sw Go Inspector
        module list
        module switch Inspector Go
        module list



Try loading a module and unload another

.. code::

        module purge
        module load Go Inspector
        module load intel
        module list
        module unload Inspector
        module list



Try loading and unloading a module in one command.

.. code::

        module purge
        module load Go Inspector
        module load intel unload Inspector

You should get an error, try this

.. code::

        module purge
        module load Go Inspector
        ml intel -Inspector
        module list

Tired of typing ``module``, use the ``ml`` command which operates on module files similar to ``module`` command though
there are slight differences that may be worth noting

Try listing modules using both commands

.. code::

      module purge
      module load intel
      ml
      module list


Try loading modules

.. code::

        module purge
        module load intel
        ml Go

Try purging modules

.. code::

        ml intel
        ml
        module purge
        ml
        ml intel
        ml purge
        ml

Try loading & unloading multiple modules in one command

.. code::

        ml purge
        ml GCC Go Java Anaconda3
        ml intel Anaconda2 -Anaconda3 -Go




