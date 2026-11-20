f=open("names.txt")
names=f.read().splitlines()
f.close()

list=[]

for name in names:
    list.append(name)

print("Before sorting : ",end=" ")
print(list)

list.sort()
print("After sorting : ",end=" ")

print(list)


