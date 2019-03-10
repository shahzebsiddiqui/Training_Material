help([[Introspection function and executing shell example]])

-- Lmod introspection functions
local name = myModuleName()
local fname = myModuleFullName()
local version = myModuleVersion()
local filename = myFileName()
local shell = myShellName()

LmodMessage("module name:" .. name)
LmodMessage("Full Module Name:" .. fname)
LmodMessage("version:" .. version)
LmodMessage("filename:" .. filename)
LmodMessage("shell:" .. shell)

-- running command upon load a module
execute{cmd="hostname",modeA={"load"}}
execute{cmd="whoami",modeA={"load"}}
