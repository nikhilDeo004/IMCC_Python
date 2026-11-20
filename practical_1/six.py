f=open("names.txt")
names=f.read().splitlines()
f.close()

list=[]
for name in names :
    if "l" in name.lower():
        list.append(name)

print(list)