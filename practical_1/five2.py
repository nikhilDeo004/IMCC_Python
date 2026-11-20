f=open("names.txt")
names=f.read().splitlines()
f.close()

names2=sorted(set(names))

print(names2)