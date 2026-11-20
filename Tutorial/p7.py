n=int(input("Please tell how many movies you want to enter : "))

print("Enter ",n," Movie  names ")

movies=[]
for i in range (n):
    mov=input("Enter "+str(i+1)+" movie name : ")
    movies.append(mov)

print(movies)
