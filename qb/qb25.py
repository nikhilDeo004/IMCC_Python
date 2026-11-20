new1=[1,2,3,4,5,5,5,4]
new2=[]

for x in new1:
    if x not in new2:
        new2.append(x)

print(new2)