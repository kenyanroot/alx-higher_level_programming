#!/bin/bash

# Get the URL from the command line argument
url=$1

# Use curl to send a request to the URL and get the size of the response body
size=$(curl -s -o /dev/null -w "%{size_download}" "$url")

# Display the size in bytes
echo "$size"