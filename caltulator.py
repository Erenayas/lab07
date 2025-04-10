import math_utils

operations = {
    '+': math_utils.add,
    '-': math_utils.subtract,
    '*': math_utils.multiply,
    '/': math_utils.divide,
    '**': math_utils.power,
    '%': math_utils.mod
}


def calculate():
    try:
       
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /, **, %): ")

        if operator in operations:
            result = operations[operator](num1, num2)
            print(f"The result of {num1} {operator} {num2} is: {result}")
        else:
            print("Invalid operator! Please use one of the following: +, -, *, /, **, %.")
    
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calculate()
