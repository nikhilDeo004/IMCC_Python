f=open("names.txt")
names=f.read().splitlines()
f.close()

for name in names :
    d={
        "Name":name,
        "Length": len(name),
        "First Character":name[0],
        "Last Character":name[-1],
        "Palindrome": name.lower()==name[::-1].lower()
    }
    print(d)