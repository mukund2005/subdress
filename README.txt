=====================================================
                   Subdress
          Subdomain Enumerating Tool
=====================================================

Overview:
---------
Subdress is a powerful subdomain enumerating tool designed to help users identify valid and reachable subdomains for a given domain. This tool uses both DNS resolution and HTTP status checks to ensure the discovered subdomains are valid and responsive.

Features:
---------
- DNS resolution using dnspython
- HTTP status code checks using requests
- Multi-threading for faster performance
- Visual progress bar using tqdm
- Attractive ASCII art banners using pyfiglet
- Command-line interface for ease of use
- Automatically save valid subdomains to a file

Installation:
-------------
1. Update package list and upgrade all packages:
   sudo apt update && sudo apt upgrade -y

2. Install Python and pip if not already installed:
   sudo apt install -y python3 python3-pip

3. Install required Python modules:
   pip3 install dnspython requests tqdm pyfiglet termcolor

Usage:
------
1. Run the script with the domain as a command-line argument:
   python subdomain_scanner.py example.com

2. The tool will read the wordlist from 'subdword.txt' and start scanning for subdomains.

3. Valid and reachable subdomains will be displayed on the screen and saved to 'found_subdomains.txt'.

Note:
-----
- Ensure you have the wordlist file 'subdword.txt' in the same directory as the script.
- The script requires an active internet connection to perform DNS resolution and HTTP status checks.

Credits:
--------
Developed by Mukund and Copilot

Contact:
--------
For any issues or inquiries, please contact Mukund at [your email address].

=====================================================
                   Happy Scanning!
=====================================================
