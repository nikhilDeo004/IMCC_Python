f=open("names.txt")
names=f.read().splitlines()
f.close()

names=list(set(names))
names.sort(key=len)

o=open("processed_names.txt","w")
for name in names:
    o.write(name+"\n")

o.close()