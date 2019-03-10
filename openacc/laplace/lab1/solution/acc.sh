#!/bin/bash  
#SBATCH -A gue998
#SBATCH --job-name="laplace2d_acc"  
#SBATCH --output="laplace2d_acc.%j.%N.out"  
#SBATCH --partition=gpu-shared
#SBATCH --nodes=1  
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --reservation=openacc_jun_2015
#SBATCH --export=ALL  
#SBATCH -t 01:00:00  

#Executable
module load pgi/15.4
module load cuda
nvprof ./laplace2d_acc
