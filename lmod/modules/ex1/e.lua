help([[conditional load example]])

-- load module only if it is not loaded
if not isloaded("a") then
	load("a")
end

if not isloaded("b") then
	load("b")
end
