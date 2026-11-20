def execution_time(func):
    def wrapper():
        print("Function started")
        print(func())
        print("Function finished")
    return wrapper
@execution_time
def factorial():
    n=int(input("Enter a number:"))
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
factorial()