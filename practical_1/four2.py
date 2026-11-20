f=open("names.txt")
names=f.read().splitlines()
f.close()

n=open("new1.txt","w")
for name in names :
    if len(name) > 5 :
        n.write(name+"\n")

n.close()
