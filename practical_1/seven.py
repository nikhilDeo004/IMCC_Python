f=open("names.txt")
names=f.read().splitlines()
f.close()

dict={}

for name in names :
    dict[name]=dict.get(name,0)+1

print(dict)