#!/usr/bin/env python3

# Script Name:                  Ops 301 - Challenge 07
# Author:                       Amleset Tesfamariam, CF Ops lecture 301
# Date of latest revision:      09/05/2023
# Purpose:                      To create a script in Python that displays all directories and files within.
# Reason:                       Finding and listing directories/files can be helpful for troubleshooting.


# Import libraries
import os

# Declaration of variables

# Script must ask the user for a file path and read a user input string into a variable
user_input = input("Name a directory from the home folder: ")

# Script must enclose the os.walk() function within a python function that hands it the user input file path
def list_files_and_directories(directory_name):
    
    # Script must use the os.walk() function from the os library
    for (root, dirs, files) in os.walk(directory_name):
        ### Add a print command here to print ==root==
        print("==root==") 
        print(root)
        ### Add a print command here to print ==dirs==
        print("==dirs==")
        print(dirs)
        ### Add a print command here to print ==files==
        print("==files==")
        print(files)


# Invoke the function
list_files_and_directories(user_input)


# End