help([[Gaussian module in Lua ]])

local name = myModuleName()
local ver = myModuleVersion()
local root = pathJoin("/hpc/grid/gridbck4/software/apps/Linux-x86_64-RHEL7",name,ver)

setenv("g16root",root)						-- setenv g16root $base
setenv("_DSM_BARRIER","SHM")					-- setenv _DSM_BARRIER SHM
setenv("GAUSS_ARCHDIR", pathJoin(root,"g16/arch"))		-- setenv GAUSS_ARCHDIR $base/g16/arch
setenv("G09BASIS", pathJoin(root,"g16/basis"))			-- setenv G09BASIS $base/g16/basis
setenv("GAUSS_BSDDIR", pathJoin(root,"g16/bsd"))		-- setenv GAUSS_BSDDIR $base/g16/bsd
setenv("GAUSS_LEXEDIR",pathJoin(root,"g16/linda-exe"))		-- setenv GAUSS_LEXEDIR $base/g16/linda-exe
setenv("GV_DIR",pathJoin(root, "gv"))				-- setenv GV_DIR $base/gv
setenv("PGI_TERM","trace,abort")				-- setenv PGI_TERM trace,abort


prepend_path("GAUSS_EXEDIR",pathJoin(root,"g16")) 		-- prepend-path GAUSS_EXEDIR $base/g16
prepend_path("GAUSS_EXEDIR",pathJoin(root,"g16/bsd"))		-- prepend-path GAUSS_EXEDIR $base/g16/bsd
prepend_path("GAUSS_EXEDIR",pathJoin(root,"g16/local"))		-- prepend-path GAUSS_EXEDIR $base/g16/local
prepend_path("GAUSS_EXEDIR",pathJoin(root,"g16/extras"))	-- prepend-path GAUSS_EXEDIR $base/g16/extras

prepend_path("PATH", pathJoin(root, "g16"))  		-- prepend-path PATH $base/g16
prepend_path("PATH", pathJoin(root, "g16/bsd"))		-- prepend-path PATH $base/g16/bsd
prepend_path("PATH", pathJoin(root, "g16/local"))	-- prepend-path PATH $base/g16/local
prepend_path("PATH", pathJoin(root, "g16/extras")) 	-- prepend-path PATH $base/g16/extras

prepend_path("LD_LIBRARY_PATH", pathJoin(root,"g16"))		-- prepend-path LD_LIBRARY_PATH $base/g16
prepend_path("LD_LIBRARY_PATH", pathJoin(root,"g16/bsd")) 	-- prepend-path LD_LIBRARY_PATH $base/g16/bsd
prepend_path("LD_LIBRARY_PATH", pathJoin(root,"g16/extras"))	-- prepend-path LD_LIBRARY_PATH $base/g16/extras
prepend_path("LD_LIBRARY_PATH", pathJoin(root,"g16/local"))	-- prepend-path LD_LIBRARY_PATH $base/g16/local
