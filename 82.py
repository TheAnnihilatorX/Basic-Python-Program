#WAP in py to demonstare how decorators work

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
print("82.This code is written by Raghavv Gupta ERP- 0221BCA032")