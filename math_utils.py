
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

if __name__ == "__main__":
    print("Testing the math_utils module")

   
    print("Add:", add(13, 7))        
    print("Subtract:", subtract(15, 5))  
    print("Multiply:", multiply(7, 8))  
    try:
        print("Divide:", divide(20, 0))  
    except ZeroDivisionError as e:
        print(e)
    print("Power:", power(3, 4))  
    print("Mod:", mod(10, 3))    
