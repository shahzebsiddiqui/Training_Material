#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <openacc.h>

void matvec(float * restrict v, float * restrict x, float * restrict a, int i, int n)
{
  float sum = 0;
  for (int j = 0; j < n; j++)
    sum += a[i*n+j]*v[j];

  x[i] = sum;
}
int main()
{

  int N = 20000;
  int i,j;
  float *A, *V, *X;
  double start,end,time;
  double MFLOPS;
  A = (float*)malloc(sizeof(float)*N*N);
  V = (float*)malloc(sizeof(float)*N);
  X = (float*)malloc(sizeof(float)*N);

  printf("Matrix Vector Multiplication of [%d,%d] X [%d]\n ", N,N,N);

  for (i = 0; i < N; i++)
  {
    for (j = 0; j < N; j++)
      A[i*N+j] = i+j;
  
    V[i] = i+j;
  }
  start = clock();
  for (i = 0; i < N; i++)
  {
    matvec(V,X,A,i,N);
  }
  end = clock();
  time = (end-start)/CLOCKS_PER_SEC;
  MFLOPS = (N*N) / (1E6 * time);
  printf("Execution: %f sec \n", time);
  printf("MFLOPS/sec : %f\n", MFLOPS);
  return 0;
}
