import re

def analyze_log(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Log file not found!")
        return

    failed_logins = 0
    suspicious_ips = set()
    sensitive_access = 0

    for line in lines:
        if "Failed password" in line or "authentication failure" in line:
            failed_logins += 1
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                suspicious_ips.add(ip_match.group(1))

        if "/etc/passwd" in line or "/admin" in line:
            sensitive_access += 1

    print(f"Failed login attempts: {failed_logins}")
    print(f"Suspicious IPs: {', '.join(suspicious_ips) if suspicious_ips else 'None'}")
    print(f"Sensitive access attempts: {sensitive_access}")
