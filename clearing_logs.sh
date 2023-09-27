#!/bin/bash

# Script Name:                  Ops 301 - Challenge 05
# Author:                       Amleset Tesfamariam, CF Ops lecture 301, ChatGPT
# Date of latest revision:      09/01/2023
# Purpose:                      To clear a log using a bash script.
# Reason:                       It is critical as an administrator to be able to maintain clear and organized logs.


# Declaration of variables

# Creating and defining backup directory
mkdir -p "$backup_dir"
backup_dir="/var/log/backups"

# File name contains timestamp with the following format =YYYYMMDDHHMMSS
timestamp=$(date "+%Y%m%d%H%M%S") 

# Log files to backup
log_files=("/var/log/syslog" "/var/log/wtmp")

# Compressing the file size
gzip "$log_file"

# Clear the contents of the log file
> "$log_file"

# Prints to the screen the file size of the log files before compression
compressed_size=$(du -h "$backup_dir/$(basename "$log_file")-$timestamp.gz" | cut -fi)

# Prints to the screen the file size of the compressed file
echo "Initial Size of $log_file is: $initial_size"
echo "Compressed Size of $(basename "$log_file")-$timestamp.gz is: $compressed_size"

done


# End