module foo
contains

subroutine matvec(A,V,X,i,N)
        !$acc routine vector 
        implicit none
        integer, intent(in) :: i
        integer, intent(in) :: N
        real(4) :: A(N*N), V(N), X(N)
        real :: sum
        integer :: j
        sum = 0
        !$acc loop vector reduction(+:sum)
        do j=1,n
          sum = sum + a((i-1)*N+j)*v(j)
        enddo
        !$acc end loop

        X(i) = sum
end subroutine matvec
end module foo

program nestedparallel
        use cudafor
        use openacc 
        use foo
        implicit none
        
        integer :: N= 20000
        integer :: i,j,ret
        real(4), dimension(:), allocatable :: A,V,X
        real :: time, MFLOPS
        type(cudaEvent) :: event1, event2

        !#ifdef _OPENACC
          call acc_init(acc_device_nvidia)
        !#endif
        
        ret = cudaEventCreate(event1)
        ret = cudaEventCreate(event2)

        write(*,"(A,I5,A,I5,A,I5,A)") "Matrix Vector Multiplication of [",N,",",N,"] X [",N,"]"

        allocate(A(N*N))
        allocate(V(N))
        allocate(X(N))
        ! Record Start time
        ret = cudaEventRecord(event1,0)
        !$acc enter data create(A(0:N*N),V(0:N),X(0:N))
     
        !$acc parallel loop gang present(A(0:N*N),V(0:N),X(0:N))
        do i=1,N
          !$acc loop vector
          do j=1,N
            A((i-1)*N+j) = i+j
          enddo
          V(i) = i+j
        enddo

        !$acc parallel loop present(A(0:N*N),V(0:N),X(0:N)) &
        !$acc num_gangs(512) vector_length(192)
        do i=1,N
          CALL matvec(A,V,X,i,N)
        enddo
        !$acc exit data copyout(X(0:N)) delete(A(0:N*N),V(0:N),X(0:N))

        ! Record Stop time
        ret = cudaEventRecord(event2,0)
        
        ! Synchronize Events for timing
        ret = cudaEventSynchronize(event2)

        ! Record time in millisecond        
        ret = cudaEventElapsedTime(time,event1,event2)

        ! Destroy CUDA Event Object        
        ret = cudaEventDestroy(event1)
        ret = cudaEventDestroy(event2)
        MFLOPS = (N*N) / (1E6 * (time/1000.0))
        print '("Execution Time: ",f6.3, " seconds ")', time/1000.0
        print *, "MFLOPS/sec: ", MFLOPS

end program nestedparallel


