#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <openacc.h>
#include <cuda_runtime.h>
#pragma acc routine vector
void matvec(float * restrict v, float * restrict x,  float * restrict a, int i, int n)
{
  float sum = 0;
  #pragma acc loop vector reduction(+:sum)
  for (int j = 0; j < n; j++)
    sum += a[i*n+j]*v[j];

  x[i] = sum;
}
int main()
{
#ifdef _OPENACC
  acc_init(acc_device_nvidia);
#endif

  int N = 20000;
  int i,j;
  float *A, *V, *X;
  cudaEvent_t event1, event2;
  double MFLOPS;

  A = (float*)malloc(sizeof(float)*N*N);
  V = (float*)malloc(sizeof(float)*N);
  X = (float*)malloc(sizeof(float)*N);

  cudaEventCreate(&event1);
  cudaEventCreate(&event2);

  printf("Matrix Vector Multiplication of [%d,%d] X [%d]\n ", N,N,N);
  cudaEventRecord(event1,0);
  #pragma acc enter data create(A[0:N*N],V[0:N],X[0:N]) 
  
  #pragma acc parallel loop gang present(A[0:N*N],V[0:N],X[0:N]) 
  for (i = 0; i < N; i++)
  {
    #pragma acc loop vector
    for (j = 0; j < N; j++)
      A[i*N+j] = i+j;

    V[i] = i+j;
  }
    
  #pragma acc parallel loop num_gangs(512) vector_length(192) present(A[0:N*N],V[0:N],X[0:N]) 
  for (i = 0; i < N; i++)
  {
    matvec(V,X,A,i,N);
  }
  
  #pragma acc exit data copyout(X[0:N]) delete(A[0:N*N],V[0:N],X[0:N])
  cudaEventRecord(event2,0);
  cudaEventSynchronize(event2);

  float time_ms = 0;
  // get time in millisecond
  cudaEventElapsedTime(&time_ms,event1,event2);
  
  //destroy cuda event object
  cudaEventDestroy(&event1);
  cudaEventDestroy(&event2);
  
  MFLOPS = (N*N) / (1E6 * (time_ms/1000.0));
  printf("Execution: %f sec \n", time_ms/1000.0);
  printf("MFLOPS/sec : %f\n", MFLOPS);
  return 0;
}
