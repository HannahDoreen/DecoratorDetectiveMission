import functools

#Baseline code
def add(a,b):
    return (a + b)

add(5,3)

#decoratorfunction
def Log_activity(func):
    @functools.wraps(func)
    def wrapper(args,kwargs):
        print(f"Activity detected:calling {func.__name__}")# with args {args} and kwargs {kwargs}")
        result = func(args,kwargs)
        print(f"The result of operation is: {result}")
        return result
    
    return wrapper

@Log_activity
def add(a,b):
    return (a + b)

add(5,3)

@Log_activity
def subtract(a,b):
    return (a - b)

subtract(5,3)

@Log_activity
def multiply(a,b):
    return (a * b)

multiply(5,3) 

while True:
    choice = input("enter an operation (add/subtract/multiply/exit): ")
    if choice.lower() == 'exit':
        break
    a = 0
    b = 0
    try:
        a = int(input("first number: ")) 
        b = int(input("second number: "))
    except ValueError:
        print("input must be a number")

    print(a,b)
    if choice =="add":
        add(a,b)
    elif choice == "subtract":
        subtract(a,b)
    elif choice == "multiply":
        multiply(a,b)
    else:
        print("INVALID CHOICE!")

