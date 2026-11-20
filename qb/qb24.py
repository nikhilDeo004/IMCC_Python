nums=list(map(int,input("Numbers : ").split()))

first=second=None
for x in nums:
    if first is None or x>first:
        first,second=x,first
    elif x!=first and (second is None or x>second):
        second=x
print(second)