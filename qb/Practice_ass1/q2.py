f=open("names.txt","r")
names=f.read().splitlines()
f.close()

failed = 0                              # counter starts at 0
for i in range(len(names)):             # i = 0,1,2... (index of each student)
    if marks[i] < 40:                   # failed student?
        failed += 1                     # count him
        continue                        # skip the print, jump to next student
    print(names[i], marks[i])           # reached only by passed students
print("Failed:", failed)