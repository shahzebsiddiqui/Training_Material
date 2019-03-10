help([[Go help]])

local root="/nfs/grid/software/RHEL7/easybuild/software/Core/Go/1.9/"
local user = os.getenv("USER")
local group = "hpcswbuild"

if mode() == "load" then
	if userInGroup(group) then
		LmodMessage("User " .. user .. "is able to load this module")
		prepend_path("PATH",pathJoin(root,"bin"))
		prepend_path("LD_LIBRARY_PATH",pathJoin(root,"bin"))
	else
		LmodMessage("User " .. user .. " cannot load this module, this module is available for group: " .. group)

	end
end

