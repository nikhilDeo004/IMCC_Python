f=open("names.txt")
names=f.read().splitlines()
f.close()

list=[]
for name in names :
    if len(name)>5:
        list.append(name)

print(list)