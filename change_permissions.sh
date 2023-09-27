#!/bin/bash

# Script Name:                  Ops 301 - Challenge 03
# Author:                       Amleset Tesfamariam, CF Ops lecture 301, ChatGPT
# Date of latest revision:      08/30/2023
# Purpose:                      To change system file permissions on a bash script.
# Reason:                       It is important to be able to change file permissions and access the directory as an administrator.


# Declaration of variables

# Prompts user for input directory path.
read -p "Enter the directory path: " dir_path

# Prompts user for input permission number (e.g. 777 to perform a chmod 777).
read -p "Enter the permissions number (e.g., 777): " permissions

# Check if the directory exists. 
if [ ! -d "$dir_path" ]; then
    echo "Directory does not exist."
    exit 1

fi

# Navigates to the directory input by the user.
cd "$dir_path"

# Changes all files permissions inside the directory to the input setting.
chmod -R "$permissions" *

# Prints to the screen the directory contents.
echo "Directory contents:"
ls -l

# Prints to the screen the new permissions settings of everything in the directory.
echo "New permissions settings:"
ls -l | awk '{print $1, $9}'



# End