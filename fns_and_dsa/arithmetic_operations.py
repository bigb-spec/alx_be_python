print("Arithmetic Operations")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Enter the operation (add, subtract, multiply, divide): ")

def  perform_operation(num1: float, num2: float, operation: str):
    """Performs basic arithmetic operations on two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation(str): The arithmetic operation to perform ('add', 'subtract', 'multiply', 'divide')
    Returns:
         float or str: Result of the operation or error message for division by zero
    """

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
result = perform_operation(num1, num2, operation)
print(f"Result: {result}")