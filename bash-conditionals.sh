#!/bin/bash

# Script Name:                  Ops 301 - Challenge 04
# Author:                       Amleset Tesfamariam, CF Ops lecture 301
# Date of latest revision:      08/31/2023
# Purpose:                      To launch a menu system using hello world, ping self, IP info, and exit on a bash script.
# Reason:                       It is crucial to be able to quickly access computer, network, and/or system information.


# Declaration of variables

while true; do 
    echo "Hello World! How can I help you today? Choose one of the following options from below: "
    echo "1. Hello World!"
    echo "2. Ping your computer"
    echo "3. Display your computer's IP information"
    echo "4. Exit"
    read choice


    if [[ $choice == 1 ]]; then
        echo "Hello World!"
        read -p "Please Press Enter to Continue"

    elif [[ $choice == 2 ]]; then
        ping -c 5 127.0.0.1
        read -p "Please Press Enter to Continue"

    elif [[ $choice == 3 ]]; then
        ifconfig
        read -p "Please Press Enter to Continue"

    elif [[ $choice == 4 ]]; then
        echo "Exiting."
        exit 0
    
    else
        echo "Invalid Choice"
        read -p "Please Press Enter to Continue"

    fi 

done

# End