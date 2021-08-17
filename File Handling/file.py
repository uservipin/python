

""":cvar
Open function -> this function return a file object.

---syntex ...open(filename,mode)
mode:
"r" - for reading file
"w" - for writing file
"a" - for append inside file
"r+" for borh reading and writing file
"""

fp = open("ref.txt", "r")
x= fp.read()
print(x)


