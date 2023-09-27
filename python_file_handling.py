#!/usr/bin/env python3

# Script Name:                  Ops 301 - Challenge 10
# Author:                       Amleset Tesfamariam, CF Ops lecture 301, ChatGPT
# Date of latest revision:      09/08/2023
# Purpose:                      To create a Python script that creates a new file, appends, writes, and deletes using file handling commands.
# Reason:                       It is important to know how to use file handling commands to readily control and access file contents.


# Declaration of variables

# Create a new .txt file and append three lines
with open("my_file.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

# Read and print the first line from the file
with open("my_file.txt", "r") as file:
    first_line = file.readline()
    print("First Line:", first_line)

# Delete the .txt file
import os
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
    print("File 'my_file.txt' has been deleted.")

else:
    print("File 'my_file.txt' does not exist.")


# End