#!/bin/bash

# Script Name:                  Ops 301 - Challenge 13
# Author:                       Amleset Tesfamariam, CF Ops lecture 301
# Date of latest revision:      09/13/2023
# Purpose:                      To create a script using Powershell to add a new user to the Active Directory.
# Reason:                       It is important to know how to create, edit, add, and remove users from the Active Directory as a network administrator.


# Declaration of variables


# Import Active Directory module
Import-Module ActiveDirectory

# Define the new user's information
$FirstName = "Franz"
$LastName = "Ferdinand"
$DisplayName = "$FirstName $LastName"
$SamAccountName = "ferdi"
$UserPrincipalName = "ferdi@GlobeXpower.com"
$Office = "Springfield, OR"
$Department = "TPS Department"
$Title = "TPS Reporting Lead"

# Define the AD Path where the new user will be created
$ADPath = "OU=Users,DC=YourDomain,DC=com"

# Create a secure password for the new user
$SecurePassword = ConvertTo-SecureString "SolarWinds123" -AsPlainText -Force

# Create the new user in AD
New-ADUser -Name $DisplayName -GivenName $FirstName -Surname $LastName -DisplayName $DisplayName -SamAccountName $SamAccountName -UserPrincipalName $UserPrincipalName -Office $Office -Department $Department -Title $Title -AccountPassword $SecurePassword -Path $ADPath -Enabled $true


# End