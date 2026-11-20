f=open("names.txt")
names=f.read().splitlines()
f.close()


for name in names :
    d={
        "Name : ":name,
        "Length : ":len(name),
        "First Character : ":name[0],
        "Last Character : ":name[-1],
        "Is Palindrome ?": name==name[::-1]
    }
    print(d)