text="    Masta reee !! Euu    "

#Removing spaces pudhun magun
print("Remove spaces : ",text.strip())

#Lower case
print("Remove spaces : ",text.lower())

#Upper case
print("Remove spaces : ",text.upper())

text=text.strip()
print("Capitalize Text : ",text.capitalize())

print(text.title())

print("Letter C occurs ",text.count("e"),"times in text")


print("Position of substring reee in text is : ",text.find("reee"))

print(text.replace("Masta","reee"))

print(text.startswith("Masta"))

print(text.endswith("reee"))

print("Simple Split : ",text.split())

words=["Kay","Vishay","???"]
print(" ".join(words))