f = open("names.txt")
names = f.read().splitlines()
f.close()

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    f = open(letter + ".txt", "w")
    for name in names:
        if name.startswith(letter):
            f.write(name + "\n")
    f.close()