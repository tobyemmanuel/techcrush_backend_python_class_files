"""
Error handling allows you to manage runtime errors (exceptions) in a clean and controlled way.
Instead of allowing your program to crash, you can catch the error, display a helpful message, 
or take corrective action.
Using try, except, else, and finally
"""

# try: Code that might raise an error is placed inside the try block.
# except: If an error occurs in the try block, it is caught by the except block.
# else: Code inside the else block is executed if no error occurs in the try block.
# finally: Code inside the finally block is always executed, regardless of whether an error occurred or not.

# Basic Example:
# try:
#     x = 10 / 0  # Division by zero
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print("Division successful.")
# finally:
#     print("Execution completed.")

# Custom exceptions

# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     return age


# try:
#     check_age(-5)
# except ValueError as e:
#     print(f"Error: {e}")

# import logging
# logging.basicConfig(
#     filename="app.log",
#     level=logging.DEBUG,
#     format= "%(asctime)s - %(levelname)s - %(message)s"
# )
# Handling Multiple Exceptions
# try:
#     # Code that might raise different exceptions
#     x = int(input("Enter a number: "))
#     y = 10 / x
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Invalid input! Please enter a valid number.")
# except Exception as e:
#     # logging.debug(e)
#     print(f"Something happened")


# Catching Multiple Exceptions in One except Block:
# try:
#     # Code that might raise different exceptions
#     x = int(input("Enter a number: "))
#     y = 10 / x
# except (ZeroDivisionError, ValueError) as e:
#     print(f"Error: {e}")
# except Exception as e:
#     print(f"Unexpected error: {e}")



# Sometimes, you may want to intentionally raise exceptions in your program. 
# This is done using the raise keyword. 
# This is particularly useful when you want to ensure that certain conditions are met before proceeding with the program.
# Raising a Built-in Exception:
# x = -5
# if x < 0:
#     raise ValueError("Value cannot be negative.")

# Raising Custom Exceptions:
# You can also define and raise your own custom exceptions by subclassing the built-in Exception class.
class CustomError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative.")
    print(f"Age: {age}")

try:
    check_age(-5)
except CustomError as e:
    print(f"Custom error occurred: {e}")


# Common Python Exception Types
# ZeroDivisionError: Raised when trying to divide by zero.
# FileNotFoundError: Raised when trying to open a file that doesn’t exist.
# ValueError: Raised when a function receives an argument of the correct type, but inappropriate value.
# IndexError: Raised when trying to access an index in a list that doesn't exist.
# KeyError: Raised when trying to access a key that doesn't exist in a dictionary.
# TypeError: Raised when trying to access a wrong data type


# Best Practices for Error Handling:
# 1.Catch Specific Exceptions
# 2.Don’t Overuse try-except
# 3.Use finally for Cleanup
# 4.Raise Custom Exceptions When Necessary

#References
# https://www.w3schools.com/python/python_ref_exceptions.asp
# https://docs.python.org/3/library/exceptions.html

# INSTRUCTIONS FOR TESTING
# 1. Launch your terminal and run the code
# 2. Run the code -> python 17_error_handling.py