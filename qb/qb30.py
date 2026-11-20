d={'name':'Nikhil','age':22}

print(d)
d['city']="Pune"

print("")

print(d)

d['age']=50

print("")

print(d)

print("")
print(d.get('phone','Not found'))

print("")
if 'phone' in d:
    print(d['phone'])
else:
    print('Not found')

del d['age']

print(list(d.keys()))
print(list(d.values()))


print("")

for k,v in d.items():
    print(k,"=",v)