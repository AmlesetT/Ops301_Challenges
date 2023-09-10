#!/bin/bash

# Script Name:                  Ops 301 - Challenge 06
# Author:                       Amleset Tesfamariam/ChatGPT
# Date of latest revision:      09/04/2023
# Purpose:                      To create a script in Python using bash commands.
# Reason:                       It is useful to be able to code in multiple languages using different commands.


# Declaration of variables

# The Python module "os" must be utilized
import os

# At least 3 variable must be declared and reference in Python
print
(f"Current User: {user}")
print(f"Current Date: {date}")
print(f"Current Time: {time}")

# The Python function print () must be used at least 3 times and include execution of the following bash commands
whoami_result = os.popen('whoami').read()
print(f"Current User: {whoami_result}")

ip_a_result = os.popen('ip a').read()
print(ip_a_result)

lshw_result = os.popen('lshw -short').read()
print(lshw_result)


# End