f = open("names.txt")
names = f.read().splitlines()
f.close()

A = open("A_names.txt", "w")
B = open("B_names.txt", "w")

for name in names:
    if name.startswith("A"):
        A.write(name + "\n")
    elif name.startswith("B"):
        B.write(name + "\n")

A.close()
B.close()