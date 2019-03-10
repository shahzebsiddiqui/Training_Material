help([[OpenMPI help]])


load(between("gcc","6.0","6.9"))

family("mpi")

pushenv("CC","mpicc")
pushenv("CXX","mpic++")
pushenv("FC","mpifort")

add_property("arch","mic")
