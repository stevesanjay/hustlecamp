# Function Decorator to Log Function Calls:

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function
def add(a, b):
    return a + b

result = add(3, 5)
print("Result:", result)