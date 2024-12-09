# DIPmap - Domain to IP Mapping & Bug Bounty Tool

DIPmap is a command-line tool designed for bug bounty hunters and penetration testers. It helps map domains to IP addresses and provides additional functionality like geolocation, server version detection, and scope checking (with HackerOne support).

## Features
- **Domain to IP Mapping**: Resolve domains to their corresponding IP addresses.
- **Server Version Detection**: Detect server versions (Apache, Nginx, Cloudflare, etc.).
- **Geolocation**: Get the geolocation (country, region, city) of the IP addresses.
- **HackerOne Scope Checking**: Check if a domain is in scope for a HackerOne bug bounty program (requires API key).

## Installation

### Prerequisites
Make sure you have Python 3.x installed. You'll also need the following Python libraries:
- `requests`
- `argparse`
- `socket`

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dipmap.git
   cd dipmap
