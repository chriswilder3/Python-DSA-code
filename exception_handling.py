# 1. Basic Exception Handling with try and except

    # try block: Contains code that might raise an exception.
    # except block: Catches and handles exceptions if they occur.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

    # Here, if dividing by zero raises a ZeroDivisionError, 
    # the code in the except block will handle it by printing a message.

# 2. Handling Multiple Exceptions

    # You can handle different exceptions in separate except blocks, 
    # allowing you to respond differently based on the error type.

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 3. Using a Generic except Block
    # To catch any exception, you can use a generic except block.
    # However, this approach is often avoided in production code since it can mask issues and make debugging difficult.

try:
    result = 10 / x
except Exception as e:  # Generic exception handler
    print("An error occurred:", e)
Using Exception as e also provides the actual exception message, which can be helpful for logging and debugging.

# 4. else Block
    # The else block runs if no exceptions were raised in the try block.
    # It’s useful for code that should execute only if the try block is successful.

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful:", result)

# 5. finally Block
    # The finally block always runs, regardless of whether an exception occurred.
    # It’s commonly used for cleanup actions, like closing files or releasing resources.

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()  # Ensure the file is closed regardless of errors

# 6. Raising Exceptions with raise
    # You can explicitly raise exceptions using the raise keyword, which is helpful for enforcing conditions within your code.

def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero.")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print("Error:", e)

# 7. Custom Exceptions
    # Define custom exception classes for specialized error handling by inheriting from the Exception class.
    # This approach is useful when you need exceptions specific to your application’s domain.

class NegativeValueError(Exception):
    """Custom exception for handling negative values."""
    pass

def square_root(x):
    if x < 0:
        raise NegativeValueError("Cannot take square root of a negative number.")
    return x ** 0.5

try:
    result = square_root(-9)
except NegativeValueError as e:
    print("Error:", e)

# 8. Exception Handling Best Practices
    # Catch specific exceptions where possible instead of a generic except to keep the error handling clear and focused.
    # Log exceptions for debugging and maintenance, especially in production.
    # Avoid using exceptions for control flow. They should handle errors, not replace standard logic.