#!/bin/bash

# Script Name:                  Ops 301 - Challenge 02
# Author:                       Amleset Tesfamariam
# Date of latest revision:      08/29/2023
# Purpose:                      To append the date and time on a bash script.
# Reason:                       It is important to be able to adjust the time/date when logs are automated.

# Declaration of variables
year=`date +%Y`
echo $year
month=`date +%m`
echo $month
day=`date +%d`
echo $day

hour=`date +%H`
echo $hour
minute=`date +%M`
echo $minute
second=`date +%S`
echo $second

echo "Current Date: $day-$month-$year"
echo "Current Time: $hour:$minute:$second"

# how to row append

# first create a file and add some lines to it
echo "Original file before append: "
cat testfile.txt

# the >> append
echo "My new string with date: `date`" >>testfile.txt
echo "Appended file: "
cat testfile.txt

# End