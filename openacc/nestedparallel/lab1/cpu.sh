#!/bin/bash

#SBATCH --job-name="nestedparallel"
#SBATCH --output="nestedparallel.%j.%N.out"
#SBATCH -A gue998
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --no-requeue
#SBATCH --export=ALL
#SBATCH -t 00:10:00


# This job will run on a single node 1 core job for 10 minutes and charged on project pen131
./nestedpar_cpu_C
