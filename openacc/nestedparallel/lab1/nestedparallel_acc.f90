module foo
contains

subroutine matvec(A,V,X,i,N)
        implicit none
        integer, intent(in) :: i
        integer, intent(in) :: N
        real(4) :: A(N*N), V(N), X(N)
        real :: sum
        integer :: j
        sum = 0
        do j=1,n
          sum = sum + a((i-1)*N+j)*v(j)
        enddo

        X(i) = sum
end subroutine matvec
end module foo

program nestedparallel
        use foo
        implicit none
        integer :: N = 20000
        integer :: i,j
        real(4), dimension(:), allocatable :: A
        real(4), dimension(:), allocatable :: V
        real(4), dimension(:), allocatable :: X
        real T1,T2,time
        real MFLOPS
        
        allocate(A(N*N))
        allocate(V(N))
        allocate(X(N))
        
        write(*,"(A,I5,A,I5,A,I5,A)") "Matrix Vector Multiplication of [",N,",",N,"] X [",N,"]"
        do i=1,N
          do j=1,N
            A((i-1)*N+j) = i+j
          enddo
          V(i) = i+j
        enddo
        
        CALL CPU_TIME(T1)
        do i=1,N
          CALL matvec(A,V,X,i,N)
        enddo    
        CALL CPU_TIME(T2)
        time = T2 - T1
        MFLOPS = (N*N) / (1E6 * time)
        print '("Execution Time: ",f6.3, " seconds ")', time
        print *, "MFLOPS/sec: ", MFLOPS
        
end program nestedparallel

