# core/output.py

def format_subject(subject):
    """Format the subject data into a human-readable string."""
    if isinstance(subject, tuple) and subject:
        return ", ".join([f"{item[0]}: {item[1]}" for item in subject])
    return None

def display_results(target, ports, ssl_info, version_info):
    print(f"Target: {target}")
    print("Open Ports:", ports)
   
    # Display Version Information
    if version_info:
        print("\nVersion Information:")
        for port, version in version_info.items():
            print(f"Port {port}: {version}")

    # Display SSL Information
    if ssl_info:
        display_ssl_info(ssl_info)

def display_ssl_info(ssl_info):
    """Display formatted SSL certificate information."""
    if 'error' in ssl_info:
        print(f"SSL Information Error: {ssl_info['error']}")
        return
    
    print("\nSSL Certificate Information:")
    print(f"Hostname: {ssl_info.get('hostname', 'N/A')}")
    print(f"Serial Number: {ssl_info.get('serial_number', 'N/A')}")
    print(f"Not Before: {ssl_info.get('notBefore', 'N/A')}")
    print(f"Not After: {ssl_info.get('notAfter', 'N/A')}")
    print(f"Signature Algorithm: {ssl_info.get('signatureAlgorithm', 'N/A')}")
    
    issuer = format_subject(ssl_info.get('issuer', {}))
    print(f"Issuer: {issuer if issuer else 'No issuer information available'}")
    
    subject = format_subject(ssl_info.get('subject', {}))
    print(f"Subject: {subject if subject else 'No subject information available'}")
