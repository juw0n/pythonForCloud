# To delete a file, you must import the OS module, and run its os.remove() function:

# Append mode "a"
j = open("toDelete.txt", "a")
j.write("This text line added by this code\n")
j.close()

import os
os.remove("toDelete.txt")

# To avoid getting an error, you might want to check if the file exists before you try to delete it:

j = open("toDelete2.txt", "a")
j.write("This text line added by this code\n")
j.close()

if os.path.exists("toDelete2.txt"):
  os.remove("toDelete2.txt")
else:
  print("The file does not exist")