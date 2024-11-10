#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <folder_name>"
  exit 1
fi

# Get the input argument
folder_name="$1"

# Replace spaces with hyphens
sanitized_name=${folder_name// /-}

# Create the folder
mkdir "$sanitized_name"

echo "Folder '$sanitized_name' created."