a=15
b=40
temp=a
a=b
b=temp
print(a)
print(b)


a=15
b=40
a,b=b,a
print(a)
print(b)

a=15
b=40
a=a+b
b=a-b
a=a-b
print(a,b)