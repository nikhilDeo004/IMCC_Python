f=open("names.txt")
names=f.read().splitlines()
f.close()

for name in names:
    if len(name)>5:
        print(name)