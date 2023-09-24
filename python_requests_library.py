#!/usr/bin/env python3

# Script Name:                  Ops 301 - Challenge 12
# Author:                       Amleset Tesfamariam, Google, ChatGPT
# Date of latest revision:      09/12/2023
# Purpose:                      To create a script using requests from the Python library.
# Reason:                       It is crucial to understand the evaluation of web server requests and responses.


# Declaration of variables

import requests


# Prompts the user to type a string input as the variable for your destination URL
url = input("Enter the destination URL: ")

# Prompts the user to select a HTTP Method of the following options: GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS
http_method = input("Select an HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

# Check if the selected HTTP Method is valid
valid_http_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
if http_method not in valid_http_methods:
    print("Invalid HTTP Method. Please choose from:", ", ".join(valid_http_methods))
else:
    # Print the entire request to be sent
    print(f"Sending {http_method} request to {url}")

    if confirmation == "yes":
        # Perform the HTTP request
        response = requests.request(http_method, url)

        # Translate status code to plain terms
        status_code_translation = {
            200: "OK",
            201: "Created",
            204: "No Content",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Site not found",
            500: "Internal Server Error"
        }

        # Print the response status code translation 
        if response.status_code in status_code_translation:
            print(f"Response Status: {response.status_code} ({status_code_translation[response.status_code]})")

        else: 
            print(f"Response Status: {response.status_code}")

        # Print response header information
            print("Response Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
            
    else:
        print("Request canceled.")



# End