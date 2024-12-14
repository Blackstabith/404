import ssl
import socket
from datetime import datetime

def analyze_ssl(target):
    ssl_info = {}
    try:
        # Try to establish an SSL connection
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=target)
        conn.settimeout(5.0)
        conn.connect((target, 443))

        # Get the certificate
        cert = conn.getpeercert()

        # Populate ssl_info with certificate details
        ssl_info["hostname"] = target
        ssl_info["serial_number"] = cert.get("serialNumber", "N/A")
        
        # Update the format to match the certificate's date format
        ssl_info["notBefore"] = datetime.strptime(cert["notBefore"], "%b %d %H:%M:%S %Y GMT")
        ssl_info["notAfter"] = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y GMT")
        
        ssl_info["signatureAlgorithm"] = cert.get("signatureAlgorithm", "N/A")
        
        # Format issuer and subject for better readability
        ssl_info["issuer"] = format_subject(cert.get("issuer", []))
        ssl_info["subject"] = format_subject(cert.get("subject", []))

        # Return SSL information
        return ssl_info

    except Exception as e:
        ssl_info["error"] = f"Unexpected error: {str(e)}"
        return ssl_info


def format_subject(subject):
    """Helper function to format issuer and subject fields"""
    formatted = []
    for field in subject:
        for field_name, value in field:
            formatted.append(f"{field_name}: {value}")
    return ", ".join(formatted)

def display_ssl_info(ssl_info):
    """Function to display SSL info in a clean format"""
    if "error" in ssl_info:
        print(f"SSL Information: {ssl_info['error']}")
    else:
        print("\nSSL Certificate Information:")
        print(f"Hostname: {ssl_info['hostname']}")
        print(f"Serial Number: {ssl_info['serial_number']}")
        print(f"Not Before: {ssl_info['notBefore']}")
        print(f"Not After: {ssl_info['notAfter']}")
        print(f"Signature Algorithm: {ssl_info['signatureAlgorithm']}")
        print(f"Issuer: {ssl_info['issuer']}")
        print(f"Subject: {ssl_info['subject']}")

