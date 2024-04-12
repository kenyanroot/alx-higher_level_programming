#!/bin/bash
# Sends a request to the provided URL and displays the size of the response body in bytes

url=$1
size=$(curl -s -o /dev/null -w "%{size_download}" "$url")
echo "$size"