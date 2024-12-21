# method with params

def add(num1,num2):
    adding  = num1+num2
    sub     = num1 - num2
    mult    = num1 * num2
    
    print(f" adding result : {adding}")
    print(f"sub result : {sub}")
    print(f"mult result : {mult}")
    


def call_add_method():
    add(num1=12,num2=13)

call_add_method()
