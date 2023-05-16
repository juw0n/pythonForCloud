# "a" - Append - will append to the end of the file, create the file if not exist
# "w" - Write - will overwrite any existing content. it also reate the file if not exist

# Append mode "a"
j = open("write1.txt", "a")
j.write("This text line added by this code\n")
j.close()

# Wite mode "w"
k = open("write2.txt", "w")
k.write("This text line override the existing text\n")
k.close()