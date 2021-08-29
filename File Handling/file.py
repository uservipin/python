

""":cvar
Open function -> this function return a file object.

---syntex ...open(filename,mode)
mode:
"r" - for reading file
"w" - for writing file
"a" - for append inside file
"r+" for borh reading and writing file
"""

file = open("ref.txt", "r")
# x= file.read()
y = file.readlines()



# print(x)
print(y)


