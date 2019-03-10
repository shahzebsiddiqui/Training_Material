day 3
======

Exercise: LSF/Slurm Jobscript builder 
---------------------------------------

In this exercise you will be using python script to write a job script for LSF and SLURM resource scheduler. The script
will write the job script and automatically submit the job to the scheduler.

Usage
------

::

    [siddis14@prometheus day3]$ python scheduler.py --help
    usage: scheduler.py [-h] [-t {slurm,lsf}] -W WALLTIME -N NODES -T TASKS
                        [-R RESOURCE] [-c {uptime,hostname}] [-f FILE] [-s]

    scheduler script generator

    optional arguments:
      -h, --help            show this help message and exit
      -t {slurm,lsf}, --type {slurm,lsf}
                            scheduler type
      -W WALLTIME, --walltime WALLTIME
                            wall time
      -N NODES, --nodes NODES
                            number of nodes to allocate
      -T TASKS, --tasks TASKS
                            number of tasks to allocate
      -R RESOURCE, --resource RESOURCE
                            specify resource flag
      -c {uptime,hostname}, --command {uptime,hostname}
                            specify resource flag
      -f FILE, --file FILE  specify file to write job script
      -s, --submit          submit job to scheduler


Example
---------

The script requires ``-W`` and ``-N`` for every execution which is the walltime and number of nodes to allocate for the job. The rest
of the options are optional.

``scheduler.py`` will default to LSF but this can be changed using the ``t`` or ``--type`` flag
::

  [siddis14@prometheus day3]$ python scheduler.py -W 01:00 -N 1
  Writing to file: job.lsf
  Content of File job.lsf is the following:
  #!/bin/bash
  #BSUB -W 01:00
  #BSUB -N 1
  uptime

Here is an example of slurm job with the same options

::

  [siddis14@prometheus day3]$ python scheduler.py -W 01:00 -N 1 -t slurm
  Writing to file: job.slurm
  Content of File job.slurm is the following:
  #!/bin/bash
  #SBATCH -t 01:00
  #SBATCH -N 1
  uptime
  

To submit your job use the ``-s`` or ``--submit`` flag 

::

  [siddis14@prometheus day3]$ python scheduler.py -W 01:00 -N 1 -s
  Writing to file: job.lsf
  Content of File job.lsf is the following:
  #!/bin/bash
  #BSUB -W 01:00
  #BSUB -N 1
  uptime
  Executing Command: bsub < job.lsf
  Job <336648> is submitted to default queue <general>.
  
In this example we specify 2 nodes and 2 task and it runs the ``uptime`` command

::

  [siddis14@prometheus day3]$ python scheduler.py -W 05:00 -N 2 -T 2
  Writing to file: job.lsf
  Content of File job.lsf is the following:
  #!/bin/bash
  #BSUB -W 05:00
  #BSUB -N 2
  #BSUB -n 2
  uptime

In the next example we add resource flag and change the job file name
 
::
 
   [siddis14@prometheus day3]$ python scheduler.py -W 05:00 -N 2 -T 2 -R gpu -f job1
    Writing to file: job1.lsf
    Content of File job1.lsf is the following:
    #!/bin/bash
    #BSUB -W 05:00
    #BSUB -N 2
    #BSUB -n 2
    #BSUB -R gpu
    uptime

 

Exercise
---------

Test the following for LSF and repeat the same for slurm by using ``-t slurm`` 

1. ``python scheduler.py -W 05:00 -N 2``
2. ``python scheduler.py -W 05:00 -N 2 -T 2``
3. ``python scheduler.py -W 05:00 -N 2 -T 2 -f job1``
4. ``python scheduler.py -W 05:00 -N 2 -T 2 -f job1 -s``
5. ``python scheduler.py -W 05:00 -N 2 -T 2 -R gpu -c hostname -s``

