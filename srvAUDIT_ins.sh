#!/bin/bash

# Install Python and pip (package manager for Python)
sudo apt update
sudo apt install -y python3 python3-pip

# Install required Python packages (subprocess is already part of Python standard library)
sudo pip3 install datetime logging

# Install necessary system utilities (e.g., net-tools for ifconfig, lsof, etc.)
sudo apt install -y net-tools lsof

# Run the security audit Python script
python3 security_audit_script.py

# Note: Replace "security_audit_script.py" with the actual filename of your Python script

# Clean up: Optional, you can remove this if you want to keep the audit results
# sudo rm -rf audit_results_*

# End of the script
