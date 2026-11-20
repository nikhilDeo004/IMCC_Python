sentence = input("Please enter a sentence : ")

print(sentence)

words=sentence.split()
print("Words : ",words)

if words:
    longest=max(words,key=len)
    print("Longest word : ",longest)
else:
    print("No words were entered")
