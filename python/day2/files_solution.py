import os
from shutil import copy,rmtree

def get_file_ext(file):
    return os.path.splitext(file)[1]

def group_files_by_ext(files):
    """ group files by ext"""
    file_list = []
    for file in files:
        ext = get_file_ext(file)
        if ext == ".txt":
            file_list.append(file)

    print ("Files with .txt extension")
    [print (f) for f in file_list]

def group_files_by_rwx(files):
    """ group files by read, write, execute"""
    read_list = [] 
    write_list = []
    exec_list =  []
    for file in files:
        if os.access(file,os.R_OK):
            read_list.append(file)
        if os.access(file,os.W_OK):
            write_list.append(file)
        if os.access(file,os.X_OK):
            exec_list.append(file)

    return (read_list,write_list,exec_list)

def copy_files_by_rwx(read,write,exec):
    """ copy files based on perm to the appropriate location"""
    os.chdir(os.getenv("HOME"))
    os.makedirs("read",exist_ok=True)
    os.makedirs("write",exist_ok=True)
    os.makedirs("execute",exist_ok=True)

    for f in read:
        dest = os.path.join("read",os.path.basename(f))
        print(f"Copying file {f} to {dest}")
        copy(f,dest)

    for f in write:
        dest = os.path.join("write",os.path.basename(f))
        print(f"Copying file {f} to {dest}")
        copy(f,dest)

    for f in exec:
        dest = os.path.join("execute",os.path.basename(f))
        print(f"Copying file {f} to {dest}")
        copy(f,dest)

def get_hidden_files(files):
    """ return hidden files """
    hidden = []

    for f in files:
        fname = os.path.basename(f)
        if fname.startswith("."):
            hidden.append(f)
    return (hidden)        
def symlink_hidden(files):
    """ generate symbolic link for all hidden files in directory hidden"""
    hidden = get_hidden_files(files)
    os.chdir(os.getenv("HOME"))
    rmtree("hidden")
    os.makedirs("hidden",exist_ok=True)
    for f in hidden:
        link_name = os.path.basename(f)
        link_name = link_name[1:]
        print(f"Creating Symbolic Link for file {f} at {os.path.join('hidden',link_name)}")
        os.symlink(f,os.path.join("hidden",link_name))

if __name__ == "__main__":
    """ start of program """ 
    home_dir = os.getenv("HOME")
    os.chdir(home_dir)

    # return all files in $HOME directory with full path and exclude all directories
    files = [ os.path.abspath(f) for f in os.listdir(home_dir) if os.path.isfile(os.path.abspath(f)) ]

    group_files_by_ext(files)
    read,write,exec = group_files_by_rwx(files)
    copy_files_by_rwx(read,write,exec)

    symlink_hidden(files)
