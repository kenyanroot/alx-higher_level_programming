#!/bin/bash


# Check if PYCODE variable exists and is not empty
if [ -z "$PYCODE" ]; then
    echo "PYCODE environment variable is not set or empty"
    exit 1
fi

# Execute the Python code from the PYCODE environment variable
python3 -c "$PYCODE"
