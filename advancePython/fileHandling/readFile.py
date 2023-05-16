# read file by file name
f = open("jay.txt", "r")
print(f.read())
f.close()

# read file by full file path
g = open("/home/juwon/Desktop/cloudComputingLessons/pythonForCloud/advancePython/fileHandling/thankYouLord.txt", "r")
print(g.read())
g.close()

# read a file with specific encoding
# h = open("home/juwon/Desktop/cloudComputingLessons/pythonForCloud/advancePython/fileHandling/refiner.txt", mode="r", encoding="utf-8")
# print(h.read())
# h.close()

# Read Only Parts of the File
f = open("jay.txt", "r")
print(f.read(10))
f.close()

# Loop through the file line by line:
g = open("thankYouLord.txt", "r")
for i in g:
    print(i)
g.close()

# Read one line of the file:
f = open("jay.txt", "r")
print(f.readline())
print(f.readline())
f.close()
