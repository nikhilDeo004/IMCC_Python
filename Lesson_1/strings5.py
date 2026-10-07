s = input("Enter your name : ")

l = len(s)

print("Length of string is ",l)

d=l//2

print("Half is ",d)

first_half = s[:d]
second_half = s[d:]
print("First half is ",first_half)
print("Second half is ",second_half)