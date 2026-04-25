# Conditional Statements
# Syntax

# indentation is very important in Python

# if condition:
# Code block
# elif another_condition:
# Code block
# else:
# Code block

# Example
# age = int(input("Enter your age: "))

# if age < 18:
#     print("You are a minor.")
# elif 18 <= age <= 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")


# Logical Operators
# Combine multiple conditions with and, or, and not.

# x = 4

# if age > 18 and age < 30:
#     print("Young adult")

# if age == 25 or age == 50:
#     print("Jubilee Celebration")

# print("\n================================")
# gender = str(input("Enter your gender: "))

# if age == 25:
#     if gender == "male":
#         print("You should be a dad by now")
#         if x == 4:
#             print("You should have four kids by now")
#     elif gender == "female":
#         print("You should be a mom by now")
# else:
#     print("You should be happy with yourself")


# match case
r = 5
match r:
    case 5:
        print("ok")
        pass
    case 6:
        print("not ok")
        print("it is a six")
        pass

# INSTRUCTIONS FOR TESTING
# 1. Launch your terminal and run the code
# 2. Run the code -> python 12_conditional_statements.py
