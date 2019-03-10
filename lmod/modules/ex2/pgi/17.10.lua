help([[pgi help]])

family("compiler")
add_property("arch","gpu")


pushenv("CC","pgcc")
pushenv("CXX","pg++")
pushenv("FC","pgfortran")
