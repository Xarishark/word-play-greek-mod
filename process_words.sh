#!/bin/bash

# Check if Python is installed
if ! command -v python &> /dev/null
then
    echo "Python could not be found. Please install Python to run this script."
    exit 1
fi

echo "Running word processing script..."
python process_words.py

if [ $? -eq 0 ]; then
    echo "Processing complete!"
else
    echo "An error occurred during processing."
    exit 1
fi
