f=open("names.txt")
names=f.read().splitlines()
f.close()

counter=0
for name in names :
    if name[0].lower() in "aeiou":
        counter+=1

print(f"No. of people having names greater than 5 char : {counter}")
