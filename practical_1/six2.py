f=open("names.txt")
names=f.read().splitlines()
f.close()

for name in names :
    if "a" in name.lower():
        print(name)