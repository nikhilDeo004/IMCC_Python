f = open("names.txt", "r")      # open file for reading ("r" is default)
print(f.readline().strip())        # reads ONLY first line; strip() removes the \n
f.seek(0)                          # move file pointer back to the very start
lines = f.readlines()              # read ALL lines -> list of strings
f.close()                          # close the file (always!)
names = []                         # empty list for names
marks = []                         # empty list for marks
for line in lines:                 # take one line at a time
    parts = line.strip().split(",")    # "Amit,78\n" -> ["Amit", "78"]
    names.append(parts[0])             # first piece is the name
    marks.append(int(parts[1]))        # second piece is text, so convert to int
print(names)
print(marks)