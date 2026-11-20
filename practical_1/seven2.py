f=open("names.txt")
names=f.read().splitlines()
f.close()

names2=sorted(set(names))

dict={}

counter=0
for name in names :
    dict[name]=dict.get(name,0)+1

print(dict)



