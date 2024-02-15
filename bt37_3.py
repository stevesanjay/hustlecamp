# Decorator with Arguments:

def repeat(repeats):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(repeats):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(repeats=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")