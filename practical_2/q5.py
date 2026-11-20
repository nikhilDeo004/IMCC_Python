from functools import reduce

numbers=[1,2,3,4,5,6,7,8,9,10]
squares=list(map(lambda x:x**2,numbers))

print(squares)

even=list(filter(lambda x:x%2==0,numbers))
print(even)

s=reduce(lambda x,y: x+y,numbers)
print(s)