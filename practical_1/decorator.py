def decorator(func):
    def wrapper():
        print("Masta re ")
        func()
        print("Euu")
    return wrapper

def hello():
    print("Vishay ka ")

hello1=decorator(hello)
hello()


print("")

hello1()