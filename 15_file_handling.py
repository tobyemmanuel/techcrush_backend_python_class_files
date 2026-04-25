# File Handling Basics
# Opening Files
# Use the open() function to open a file.
# Always close files to free resources.


# file = open("example.txt", "r")  # Open in read mode
# content = file.read()
# print(content)
# file.close()


# File Modes
# Mode - Description
# r -	Read (default). File must exist.
# w	-   Write. Creates a new file or truncates an existing one.
# a	-   Append. Adds content to the end of the file.
# r+ -  Read and write. File must exist.
# x -   Create a new file



# Reading Files
# Methods: read(), readline(), readlines().
# with open("example.txt", "r") as file:
    # print(file.read())        # Read entire file
    # print(file.readline())    # Read one line
    # print(file.readlines())   # Read all lines as a list
    
# Writing Files
# Use write() or writelines() for writing.
# with open("example.txt", "w") as file:
    # file.write("Hello, World!\n")
    # file.writelines(["Line 1\n", "Line 2\n"])
    
    
# Appending Files
# with open("example.txt", "a") as file:
#     file.write("This is an appended line.\n")
#     file.writelines(["Appended Line 3\n", "Appended Line 4\n"])
    


# To delete a file
import os
if os.path.exists("example.txt"):
    os.remove("example.txt")

# INSTRUCTIONS FOR TESTING
# 1. Launch your terminal and run the code
# 2. Run the code -> python 15_file_handling.py
