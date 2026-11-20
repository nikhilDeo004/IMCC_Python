names=("Nikhil","Mohit","Yash")
marks=(95,99,50)

for n,m in zip(names,marks):
    print(f"{n}:{m}")

print()


pairs=tuple(zip(names,marks))
print(pairs)

print()

names2,marks2=zip(*pairs)
print(names2,marks2)