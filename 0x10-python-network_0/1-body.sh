#!/bin/bash

# Get the URL from the command line argument
url=$1

# Use curl to send a GET request to the URL and get the response body
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
body=$(curl -s "$url")

# Check the response status code and display the body if it's 200
if [ "$response" -eq 200 ]; then
    echo "$body"
fi