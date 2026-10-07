S = int(input("Enter S: "))
N = int(input("Enter N: "))
print(list(map(pow, range(S, S + N), [2] * N)))