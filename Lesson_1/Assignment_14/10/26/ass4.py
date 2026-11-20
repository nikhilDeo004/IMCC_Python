file = open("file.txt", "r")
text = file.read()
file.close()

words = text.split()

# i. Total number of words
print("Total number of words:", len(words))

# ii. All unique words
unique_words = list(set(words))
print("Unique words:", unique_words)