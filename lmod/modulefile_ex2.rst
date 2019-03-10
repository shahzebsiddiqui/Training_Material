modulefile exercise 2
=====================

Approx Time: 12 mins


Please source the following file before proceeding

.. code::

      source setup.sh


Example: Translate modulefile from TCL to LUA

.. code::

        ml purge
        ml gaussian/g16.a03.avx

Translating modules from TCL to LUA can be tedious, luckily Lmod has a script to 
convert your modules using ``tcl2lua.tcl``

Run the following on gaussian module

.. code::

   $LMOD_DIR/tcl2lua.tcl /nfs/grid/software/RHEL7/non-easybuild/modules/all/gaussian/g16.a03.avx

Example: Convert shell script to modulefile

.. code::

   $LMOD_DIR/sh_to_modulefile shell_to_lua.sh


Example: Customize default module.  check .version file

.. code::

        ml purge
        ml gcc

Example: Sticky Module

.. code::

        ml purge
        ml gcc/6.0
        # can't remove sticky module
        ml purge
        # try 
        ml --force purge

Example: Family modules

.. code::

        # gcc and pgi should automatically swap
        ml purge
        ml gcc
        echo $CC
        ml pgi
        echo $CC

Example: pushenv example

.. code::

        ml purge
        ml pgi
        echo $CC
        ml openmpi/2.0.0-pgi-17.10
        echo $CC
        ml -openmpi/2.0.0-pgi-17.10
        echo $CC

Example: load atleast example

.. code::

        ml purge
        ml openmpi/2.1.0-gcc-6.x
        ml

Example: group module example

.. code::

        ml purge
        ml Go/1.9

