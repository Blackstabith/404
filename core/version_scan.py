# core/version_scan.py
import nmap

def scan_version(target, ports):
    nm = nmap.PortScanner()
    try:
        print(f"Scanning versions for target: {target}")
        nm.scan(hosts=target, arguments=f'-p {",".join(map(str, ports))} -sV')
        
        version_info = {}
        for port in ports:
            if nm[target].has_tcp(port):
                version_info[port] = nm[target]['tcp'][port].get('version', 'N/A')
            else:
                version_info[port] = 'Closed'
        
        return version_info
    
    except Exception as e:
        return {'error': str(e)}
