#!/bin/bash

# Update package list and upgrade all packages
sudo apt update && sudo apt upgrade -y

# Install Python and pip if not already installed
sudo apt install -y python3 python3-pip

# Install required Python modules
pip3 install dnspython requests tqdm pyfiglet termcolor

# Verify installation
echo "Installed Python modules:"
pip3 list | grep -E 'dnspython|requests|tqdm|pyfiglet|termcolor'

echo "All modules installed successfully!"
