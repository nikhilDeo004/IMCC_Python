f = open("names.txt")
names = f.read().splitlines()
f.close()

names2 = list(set(names))
names2.sort(key=len)

n = open("new3.txt", "w")
for name in names2:
    n.write(name + "\n")
n.close()

n = open("new3.txt", "r")
for name in n:
    print(name, end="")
n.close()