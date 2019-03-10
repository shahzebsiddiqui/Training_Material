#!/bin/bash

#SBATCH --job-name="nestedparallel"
#SBATCH --output="nestedparallel.%j.%N.out"
#SBATCH -A gue998
#SBATCH --partition=gpu-shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --no-requeue
#SBATCH --gres=gpu:1
#SBATCH --reservation=openacc_jun_2015
#SBATCH --export=ALL
#SBATCH -t 00:10:00


# This job will run on a single node 1 core job on GPU for 10 minutes and charged on project pen131

#loading modules
module load pgi/15.4
module load cuda

nvprof ./nestedpar_C
