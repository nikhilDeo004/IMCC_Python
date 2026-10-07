s = input("Enter a string : ").lower()
total = sum(s.count(v) for v in "aeiou")
print("Vowels occur", total, "times in text")