CC = pgcc
CFORTRAN = pgfortran
CFLAGS = -Minfo=accel -ta=nvidia,time -O3 -acc -fast -Minline
BIN = nestedpar_C nestedpar_F
all: $(BIN)
nestedpar_C: nestedparallel.c
	$(CC) -o $@ $< $(CFLAGS)
nestedpar_F: nestedparallel.f90
	$(CFORTRAN) -o $@ $< $(CFLAGS)
clean:
	$(RM) $(BIN)

