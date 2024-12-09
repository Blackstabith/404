# DIPmap - Domain to IP Mapping & Bug Bounty Tool

DIPmap is a command-line tool designed for bug bounty hunters and penetration testers. It helps map domains to IP addresses and provides additional functionality like geolocation, server version detection, and scope checking (with HackerOne support).

## Features
- **Domain to IP Mapping**: Resolve domains to their corresponding IP addresses.
- **Server Version Detection**: Detect server versions (Apache, Nginx, Cloudflare, etc.).
- **Geolocation**: Get the geolocation (country, region, city) of the IP addresses.
- **HackerOne Scope Checking**: Check if a domain is in scope for a HackerOne bug bounty program (requires API key).

## Installation

### Prerequisites
Make sure you have Python 3 installed. You'll also need the following Python libraries:
- `requests`
- `argparse`
- `socket`

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Blackstabith/dipmap.git
   cd dipmap

pip install -r requirements.txt

sudo cp dipmap.py /usr/local/bin/dipmap
sudo chmod +x /usr/local/bin/dipmap


Usage

dipmap -d <domain> -I -V -G
Command Line Options:
-d, --domain: Specify the domain you want to map.
-I, --ip: Show IP addresses for the domain.
-V, --version: Show server version information (Apache, Nginx, etc.).
-G, --geolocation: Get geolocation information for the IP addresses.
(work in progress) -S, --check-scope: Check if the domain is in scope for HackerOne (requires an API key).

Example
dipmap -d google.com -I -V -G

This will:

Show the IP addresses for google.com
Fetch the server version information
Show geolocation data for the IP addresses

Contributing
Contributions are welcome! If you'd like to help improve this tool, feel free to fork the repository, create a new branch, and submit a pull request.

Reporting Issues
If you encounter any bugs or have suggestions for new features, please open an issue on GitHub
