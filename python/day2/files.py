import os
from shutil import copy,rmtree

def get_file_ext(file):
    return os.path.splitext(file)[1]

def group_files_by_ext(files):
    """ group files by ext"""
    file_list = []
    for file in files:
        # TODO: 
        # 1. get file extension 
        # 2. if file extension is ".txt" add to list


    print ("Files with .txt extension")
    [print (f) for f in file_list]

def group_files_by_rwx(files):
    """ group files by read, write, execute"""
    read_list = [] 
    write_list = []
    exec_list =  []
    for file in files:
        # TODO:
        # 1. if file has read permission add to read_list
        # 2. if file has write permission add to write_list
        # 3. if file has exec permission add to exec_list
        # hint: use os.access and os.R_OK, os.W_OK, os.X_OK

    return (read_list,write_list,exec_list)

def copy_files_by_rwx(read,write,exec):
    """ copy files based on perm to the appropriate location"""
    # TODO: change to home directory just to be safe

    # TODO: create directory read, write, execute.
    # hint: use os.makedirs. Specify argument exist_ok=True
    # See https://docs.python.org/3/library/os.html#os.makedirs for usage

    for f in read:
        # TODO: build dest path to copy file

        print(f"Copying file {f} to {dest}")

        # TODO: copy file  

    # TODO: Repeat for loop for write and exec


def get_hidden_files(files):
    """ return hidden files """
    hidden = []

    for f in files:
        # TODO: add files to list that start with leading .

    return (hidden)        
def symlink_hidden(files):
    """ generate symbolic link for all hidden files in directory hidden"""
    hidden = get_hidden_files(files)

    # TODO: change to home directory just to be safe

    # TODO: Remove $HOME/hidden directory 

    # TODO: Create $HOME/hidden directory using 

    for f in hidden:
        # TODO: build target link name without leading . in link name
        print(f"Creating Symbolic Link for file {f} at {os.path.join('hidden',link_name)}")

        # TODO: create symlink use os.symlink 

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
