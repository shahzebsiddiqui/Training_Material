#!/bin/bash  
#SBATCH -A gue998
#SBATCH --job-name="laplace2d_omp"  
#SBATCH --output="laplace2d_omp.%j.%N.out"  
#SBATCH --partition=compute  
#SBATCH --nodes=1  
#SBATCH --ntasks-per-node=24
#SBATCH --export=ALL  
#SBATCH -t 00:01:00  

#SET the number of openmp threads  
export OMP_NUM_THREADS=24

#Executable
./laplace2d_omp  
