CC = pgcc
CFORTRAN = pgfortran
CFLAGS = -Minfo=accel -ta=nvidia,time -O3 -acc -fast -Minline
BIN = nestedpar_acc_C nestedpar_acc_F nestedpar_cpu_C nestedpar_cpu_F
all: $(BIN)
nestedpar_acc_C: nestedparallel_acc.c
	$(CC) -o $@ $< $(CFLAGS)
nestedpar_acc_F: nestedparallel_acc.f90
	$(CFORTRAN) -o $@ $< $(CFLAGS)
nestedpar_cpu_C: nestedparallel_cpu.c
	$(CC) -o $@ $< -O3 -Minfo
nestedpar_cpu_F: nestedparallel_cpu.f90
	$(CFORTRAN) -o $@ $< -O3 -Minfo
clean:
	$(RM) $(BIN)

