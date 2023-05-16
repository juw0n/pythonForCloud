# Get current working directory

import os
currentWorkingDir = os.getcwd()
print("current working directory: ", currentWorkingDir)

# change directory to any path
# import os
os.chdir("/home/juwon/Downloads")
print("changed Direcory to: ", os.getcwd())
os.chdir(currentWorkingDir)
print("Back to the current working directory: ", os.getcwd())

# List all directories in a directory
# import os
print("List of directories and files: ", os.listdir("/home/juwon/Documents"))

# Create a new directory (you must import os)
# import os
if os.path.exists("newDirectory"):
    print("This directory already exist")
else:
    os.mkdir("newDirectory")
    print("The folder/Directory is created")

# renaming an existing directory
# import os
os.rename("newDirectory", "newDirectoryName")
print("The directory have been renamed")
print(os.listdir())

# Removing an empty directory
# import os
os.rmdir("newDirectoryName")
print("The empty directory have been removed")

# Removing a non-empty directory
import shutil
# shutil.rmtree("directory name or path")