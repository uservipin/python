import re
f = open('cat.txt','r')
a = f.read()
f.close()
x = re.findall(r'\bCAT\w+', a)

res = []
for i in x:
    if i not in res:
        res.append(i)
f = open("catmodified3.txt", "w")
for i in res:
    f.write(i+'\n')
f.close()

help(re)