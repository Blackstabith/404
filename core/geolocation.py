import socket
import requests

def get_ip_address(target):
    """
    Resolves the IP address for the given target.
    :param target: Domain name or hostname
    :return: IP address as a string or None if resolution fails
    """
    try:
        ip_address = socket.gethostbyname(target)
        return ip_address
    except socket.gaierror as e:
        return {"error": f"Failed to resolve IP address: {e}"}

def get_geolocation(ip_address):
    """
    Retrieves geolocation data for the given IP address using an external API.
    :param ip_address: The IP address to look up
    :return: A dictionary with geolocation data or error message
    """
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json", timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch geolocation. Status code: {response.status_code}"}
    except requests.RequestException as e:
        return {"error": f"Request failed: {e}"}
