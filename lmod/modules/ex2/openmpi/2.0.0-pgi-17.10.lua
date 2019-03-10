help([[OpenMPI help]])

if not isloaded("pgi/17.10") then
	load("pgi/17.10")
end

family("mpi")

pushenv("CC","mpicc")
pushenv("CXX","mpic++")
pushenv("FC","mpifort")

