CC = pgcc
CFORTRAN = pgfortran
CUDA_PATH = /opt/pgi/linux86-64/2015/cuda/7.0
CFLAGS = -Minfo=accel -ta=nvidia,time,cc3x -O3 -acc -fast -Minline -I$(CUDA_PATH)/include/ -L$(CUDA_PATH)/lib64 -lcudart
FFLAGS = $(CFLAGS) -lcudafor
BIN = nestedpar_C nestedpar_F
all: $(BIN)
nestedpar_C: nestedparallel.c
	$(CC) -o $@ $< $(CFLAGS)
nestedpar_F: nestedparallel.f90
	$(CFORTRAN) -o $@ $< $(FFLAGS)
clean:
	$(RM) $(BIN)

