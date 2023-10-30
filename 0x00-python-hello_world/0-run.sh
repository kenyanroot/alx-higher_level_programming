#!/bin/bash

# Check if the PYFILE environment variable is set
if [[ -z "$PYFILE" ]]; then
  echo "The PYFILE environment variable is not set."
  exit 1
fi

# Check if the specified file exists
if [[ ! -f "$PYFILE" ]]; then
  echo "The file $PYFILE does not exist."
  exit 1
fi

# Run the Python script
python3 "$PYFILE"
