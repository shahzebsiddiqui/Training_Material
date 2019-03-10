import os
import stat
import shutil

file="coords.txt"
print("splitting file by extension: " + str(os.path.splitext(file)))
print("Getting basename of file: " +  os.path.basename(file))
print("Getting parent directory:" +  os.path.dirname(file))
print("Absolute path: " + os.path.abspath(file))

abspath = os.path.abspath(file)
print("Parent Directory Path: " + os.path.dirname(abspath))
print("Parent Directory Name:" + os.path.basename(os.path.dirname(abspath)))

file="/abc"
if os.path.exists(file):
    print ("File %s exists" % file)
else:
    print("File %s does not exist" % file)

print(os.path.join("path","to","some","file"))

print(os.uname())
print (os.name)
print("environment variable $HOME: " + os.environ["HOME"])
print("current working directory:" + os.getcwd())

file="coords.txt"
fd =  open(file,"r")
content = fd.read()
print("Reading file: %s" % (file))
print(content)
new_file = "coords_write.txt"
print("Writing file %s " % (new_file))

fd1 = open(new_file,"w")
fd1.write(content)
print(os.getcwd())
os.system("ls -l " + new_file)
fd.close()
fd1.close()

if os.access(new_file, os.R_OK):
    print (f"{new_file} is readable")
else:
    print (f"{new_file} is not readable")

if os.access(new_file, os.W_OK):
    print (f"{new_file} is writable")
else:    
    print (f"{new_file} is not writable")


if os.access(new_file, os.X_OK):
    print (f"{new_file} is executable")
else:    
    print (f"{new_file} is not executable")

print (f"Changing permission for %{new_file} to 777")
os.chmod(new_file,stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
os.system("ls -l " + new_file)

print(f"Listing content of current directory {os.getcwd()}")
print(os.listdir(os.getcwd()))


new_dir = os.path.join("a","b","c")
parent_dir = os.path.basename(os.path.dirname(os.path.dirname(new_dir)))
# only create directory if it doesn't exist
if not os.path.isdir(new_dir):
    print("Creating new directory " + new_dir)
    os.makedirs(new_dir)

open("a/a.txt",'w')
open("a/b/b.txt",'w')
open("a/b/c/c.txt",'w')

print (f"Traversing Directory {parent_dir}")
for root,subdir,files in  os.walk(parent_dir):
    for file in files:
        print(os.path.join(root,file))

# only remove directory if it exists
if os.path.isdir(parent_dir):
    print("Removing directory " + parent_dir)
    try:
        os.removedirs(parent_dir)
    except OSError:
        print(f"Can't remove {new_dir} with os.removedir()")
        parent_parent_dir = os.path.basename(os.path.dirname(os.path.dirname(new_dir)))
        print(f"Let's remove directory  {parent_parent_dir} via shutil.rmtree()")
        shutil.rmtree(parent_parent_dir)

print(f"Removing {new_file}")
os.remove(new_file)
