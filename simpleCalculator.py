print("***Simple Calculator***")

first = float(input("Enter first number: "))
operator = input("Enter operator of your choice (+, -, *, /): ")
second = float(input("Enter second number:"))

try:
    match operator:
        case "+":
            result = first + second
        case "-":
            result = first - second
        case "*":
            result = first * second
        case "/":
            if second == 0:
                        raise ZeroDivisionError("Cannot divide by zero")
            result = first / second 
        case _:
            raise ValueError("Invalid operator")  

    if round(result) == result:
        print(f"The value is {int(result)}")
    else:
        print(f"The value is {result:.1f}")

except ValueError as e:
    print(f"Error: {e}")
    
except ZeroDivisionError as e:
    print(f"Error: {e}")