#Read all lines from file into a list . Print the total number of lines and display the 2nd and 4th line .

with open("file.txt","r") as file:
        lines=file.readlines()

print("Total number of lines : ",len(lines))

if len(lines) >= 2:
        print("2nd line:", lines[1])
else:
        print("The file has fewer than 2 lines.")

if len(lines) >= 4:
        print("4th line:", lines[3])
else:
        print("The file has fewer than 4 lines.")


print(lines[1])

