def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    
    return wrapper
  
@uppercase_decorator
def say_name():
    return ("my name is doreen")

print(say_name())


def upper(f):
    def w():
        return f().upper()
    return w

def exclaim(f):
    def w():
        return f() + "!"
    return w

@upper
@exclaim
def say():
    return "hi"

print(say())