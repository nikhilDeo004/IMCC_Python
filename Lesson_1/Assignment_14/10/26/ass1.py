file = open("file.txt", "r")
text = file.read()
file.close()

count = 0
for ch in text:
    if ch in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)